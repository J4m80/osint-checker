def check(response):
    if response.status_code == 404:
        return {
            "status": "not_found"
        }

    text = response.text.lower()

    not_found_markers = [
        "sorry, this page isn't available",
        "page isn't available",
        "the link you followed may be broken",
    ]

    for marker in not_found_markers:
        if marker in text:
            return {
                "status": "not_found"
            }

    found_markers = [
        '"profilepage_',
        '"username"',
        '"full_name"',
        '"biography"',
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
