from checkers import status_checker, instagram_checker, tiktok_checker


class FakeResponse:
    def __init__(self, status_code, text=""):
        self.status_code = status_code
        self.text = text


def test_status_200_is_found():
    result = status_checker.check(FakeResponse(200))
    assert result == {"status": "found"}


def test_status_404_not_found():
    result = status_checker.check(FakeResponse(404))
    assert result == {"status": "not_found"}

def test_status_500_error():
    result = status_checker.check(FakeResponse(500))
    assert result == {"status": "error", "status_code": 500}

def test_instagram_404_is_not_found():
    result = instagram_checker.check(FakeResponse(404))
    assert result == {"status": "not_found"}

def test_instagram_not_available_phrase_is_not_found():
    result = instagram_checker.check(FakeResponse(200,  "Sorry, this page isn't available"))
    assert result == {"status": "not_found"}

def test_instagram_two_profile_markers_is_found():
    result = instagram_checker.check(FakeResponse(200, '"username", "biography"'))
    assert result == {"status": "found"}

def test_instagram_one_marker_is_error():
    result = instagram_checker.check(FakeResponse(200, '"username", "hello"'))
    assert result == {"status": "error", "status_code": 200}

def test_instagram_403_is_error():
    result = instagram_checker.check(FakeResponse(403))
    assert result == {"status": "error", "status_code": 403}

def test_instagram_not_found_phrase_wins_over_profile_markers():
    result = instagram_checker.check(FakeResponse(200, '''"page isn't available","username", "biography"'''))
    assert result == {"status": "not_found"}

def test_tiktok_404_is_not_found():
    result = tiktok_checker.check(FakeResponse(404))
    assert result == {"status": "not_found"}

def test_tiktok_not_found_phrase_is_not_found():
    result = tiktok_checker.check(FakeResponse(200, "couldn't find this account"))
    assert result == {"status": "not_found"}

def test_tiktok_two_profile_markers_is_found():
    result = tiktok_checker.check(FakeResponse(200, '"uniqueid", "nickname"'))
    assert result == {"status": "found"}

def test_tiktok_one_marker_is_error():
    result = tiktok_checker.check(FakeResponse(200, '"nickname", "hi"'))
    assert result == {"status": "error", "status_code": 200}

def test_tiktok_403_is_error():
    result = tiktok_checker.check(FakeResponse(403))
    assert result == {"status": "error", "status_code": 403}
