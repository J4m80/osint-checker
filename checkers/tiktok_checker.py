def check(response):
    if response.status_code == 404:
        return {
            "status": "not_found"
        }

    text = response.text.lower()

    not_found_markers = [
        "couldn't find this account",
        "couldn't find this page",
        "page not available",
        "user not found",
    ]

    for marker in not_found_markers:
        if marker in text:
            return {
                "status": "not_found"
            }

    found_markers = [
        '"uniqueid"',
        '"nickname"',
        '"followers"',
    ]

    found_count = sum(marker in text for marker in found_markers)

    if response.status_code == 200 and found_count >= 2:
        return {
            "status": "found"
        }

    return {
        "status": "error",
        "status_code": response.status_code
    }
