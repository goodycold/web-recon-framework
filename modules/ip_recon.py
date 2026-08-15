import socket
import sys
import requests


def resolve_ip(target):
    print(f"[*] Resolving IP address for: {target}")

    try:
        ip_address = socket.gethostbyname(target)
        return ip_address

    except socket.gaierror as error:
        print(f"[!] IP resolution failed: {error}")
        return None


def get_geolocation(ip_address):
    print(f"[*] Getting basic geolocation for: {ip_address}")

    try:
        response = requests.get(
            f"https://ipinfo.io/{ip_address}/json",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"[!] Geolocation lookup failed: {error}")
        return None


def display_results(ip_address, location):
    print("\n========== IP & GEOLOCATION RESULTS ==========")

    print("\nIP Address:")

    if ip_address:
        print(f"- {ip_address}")
    else:
        print("- Not available")

    print("\nGeolocation:")

    if not location:
        print("- Not available")
        return

    fields = [
        ("Country", "country"),
        ("Region", "region"),
        ("City", "city"),
        ("Organization", "org"),
        ("Timezone", "timezone"),
    ]

    for label, field in fields:
        value = location.get(field)

        if value:
            print(f"{label}: {value}")
        else:
            print(f"{label}: Not available")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/ip_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    ip_address = resolve_ip(target)

    if ip_address:
        location = get_geolocation(ip_address)
    else:
        location = None

    display_results(ip_address, location)


if __name__ == "__main__":
    main()
