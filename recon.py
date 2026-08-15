import sys

from modules.dns_recon import run_dns_recon, display_results
from modules.whois_recon import run_whois_recon, display_results as display_whois_results
from modules.ip_recon import resolve_ip, get_geolocation, display_results as display_ip_results
from modules.http_recon import get_http_headers, display_results as display_http_results


def main():
    print("Web Recon Automation Framework")
    print("------------------------------")

    if len(sys.argv) != 2:
        print("Usage: python3 recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    print(f"Target: {target}")

    # DNS Reconnaissance
    print("\n[+] Starting DNS reconnaissance...")

    dns_results = run_dns_recon(target)
    display_results(dns_results)

    # WHOIS Reconnaissance
    print("\n[+] Starting WHOIS reconnaissance...")

    whois_results = run_whois_recon(target)
    display_whois_results(whois_results)

    # IP Address & Geolocation Reconnaissance
    print("\n[+] Starting IP address and geolocation reconnaissance...")

    ip_address = resolve_ip(target)

    if ip_address:
        location = get_geolocation(ip_address)
        display_ip_results(ip_address, location)
    else:
        print("[!] Could not resolve IP address.")

    # HTTP Response Headers Reconnaissance
    print("\n[+] Starting HTTP response headers reconnaissance...")

    http_results = get_http_headers(target)
    display_http_results(http_results)


if __name__ == "__main__":
    main()
