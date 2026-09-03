def check(response):
    if response.status_code == 200:
        return {
            "status": "found"
        }

    elif response.status_code == 404:
        return {
            "status": "not_found"
        }

    else:
        return {
            "status": "error",
            "status_code": response.status_code
        }
