import requests

from sites import sites
from checkers import status_checker
from checkers import instagram_checker
from checkers import tiktok_checker


checkers = {
    "status": status_checker.check,
    "instagram": instagram_checker.check,
    "tiktok": tiktok_checker.check,
}


def check_username(username):
    results = []

    for site in sites:
        url = site["url"].format(username=username)

        try:
            response = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
                timeout=10
            )

            checker = checkers.get(site["method"])

            if checker is None:
                results.append({
                    "site": site["name"],
                    "status": "error",
                    "url": url,
                    "error": "Unknown checker"
                })
                continue

            result = checker(response)

            result["site"] = site["name"]
            result["url"] = url

            results.append(result)

        except requests.RequestException as error:
            results.append({
                "site": site["name"],
                "status": "error",
                "url": url,
                "error": str(error)
            })

    return results
