# OSINT Username Checker

![Tests](https://github.com/J4m80/osint-checker/actions/workflows/tests.yml/badge.svg)

A command-line tool that checks whether a username exists on popular websites. Built for learning: modular design, honest result statuses and automated tests.

## How it works
For each site in `sites.py` the tool requests the profile URL and passes the response to a site-specific checker. Every site gets one of three statuses:
- `found` – the profile exists
- `not_found` – the profile does not exist
- `error` – the tool could not decide (blocked request, unexpected page, network error)

The `error` status is deliberate: when the evidence is not enough, the tool says "I don't know" instead of guessing.

## Supported sites
GitHub, GitLab, Codeberg, Dev.to, Kaggle, HackerOne, Instagram, TikTok

GitHub, GitLab, Codeberg, Dev.to, Kaggle and HackerOne are checked by the HTTP status code. Instagram and TikTok are checked by looking for markers in the page text, which is less reliable: these sites often block automated requests, and then the result is `error`.

## Example
    Enter a username: [your real username]

    Checking username: [your real username]
    ========================================
    [+] GitHub: FOUND
        https://github.com/[your real username]
    ----------------------------------------
    [-] GitLab: NOT FOUND
    ----------------------------------------
    [!] Instagram: ERROR
        HTTP status: [code]
    ----------------------------------------
    ...
    Finished. Found: [x]/8

(Replace this block with a real output from your run.)

## Install and run
    git clone https://github.com/J4m80/osint-checker.git
    cd osint-checker
    pip install -r requirements.txt
    python main.py

## Project structure
- `main.py` – user input and output
- `checker.py` – requests every site and collects results
- `sites.py` – list of sites (to add a site, add one entry)
- `checkers/` – result detection logic:
  - `status_checker.py` – by HTTP status code
  - `instagram_checker.py` – by page text markers
  - `tiktok_checker.py` – by page text markers
- `test_checkers.py` – pytest tests

## Tests
    pip install pytest
    pytest

Tests use a fake response object, so they run without internet access. They cover:
- HTTP status codes (200, 404, 403, 500)
- "page not available" phrases
- profile markers (two markers = found, one marker = error)
- priority of rules: a "not found" phrase wins over profile markers

Tests run automatically on every push with GitHub Actions.

A bug found while writing the tests: the "not found" markers in the Instagram checker were written with capital letters, while the page text is converted to lowercase before searching, so they never matched. Fixed.

## Removed sites
Pinterest and Twitch were removed from the list. In my checks they returned HTTP 200 even for non-existent usernames, so status codes are not enough for them. The page title differs (empty on Pinterest, just "Twitch" on Twitch), so they could come back with title-based checkers.

## Known limitations
- Instagram and TikTok checks depend on page text and can break when the sites change
- Username is not validated or URL-encoded yet
- Sites are checked one by one, which is slow if several time out
- `check_username` itself (network part) has no tests yet

## Roadmap
- [ ] Validate and URL-encode the username
- [ ] Custom checkers for Pinterest and Twitch (page title)
- [ ] Run requests in parallel
- [ ] Tests for `check_username` with mocked requests
- [ ] JSON export

## Disclaimer
For educational purposes and public information only. The same username on different sites does not mean it is the same person.
