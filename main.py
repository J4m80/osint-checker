from checker import check_username

username = input("Enter a username: ")

result = check_username(username)

print()
print(f"Checking username: {username}")
print("=" * 40)

found_count = 0

for site in result:
    if site["status"] == "found":
        print(f"[+] {site['site']}: FOUND")
        print(f"    {site['url']}")
        found_count += 1

    elif site["status"] == "not_found":
        print(f"[-] {site['site']}: NOT FOUND")

    else:
        print(f"[!] {site['site']}: ERROR")

        if "status_code" in site:
            print(f"    HTTP status: {site['status_code']}")

        if "error" in site:
            print(f"    Error: {site['error']}")

    print("-" * 40)

print(f"Finished. Found: {found_count}/{len(result)}")
