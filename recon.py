import sys

from modules.dns_recon import run_dns_recon, display_results
from modules.whois_recon import run_whois_recon, display_results as display_whois_results
from modules.ip_recon import resolve_ip, get_geolocation, display_results as display_ip_results
from modules.http_recon import get_http_headers, display_results as display_http_results
from modules.ssl_recon import get_ssl_certificate, display_results as display_ssl_results
from modules.tech_recon import get_technologies, display_results as display_tech_results
from modules.subdomain_recon import get_subdomains, display_results as display_subdomain_results
from modules.robots_recon import get_robots, display_results as display_robots_results
from modules.report_generator import generate_report


def main():
    print("Web Recon Automation Framework")
    print("------------------------------")

    if len(sys.argv) != 2:
        print("Usage: python3 recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    print(f"Target: {target}")

    # Store all reconnaissance results
    results = {}

    # DNS Reconnaissance
    print("\n[+] Starting DNS reconnaissance...")

    dns_results = run_dns_recon(target)
    display_results(dns_results)
    results["dns"] = dns_results

    # WHOIS Reconnaissance
    print("\n[+] Starting WHOIS reconnaissance...")

    whois_results = run_whois_recon(target)
    display_whois_results(whois_results)
    results["whois"] = whois_results

    # IP Address & Geolocation Reconnaissance
    print("\n[+] Starting IP address and geolocation reconnaissance...")

    ip_address = resolve_ip(target)

    if ip_address:
        location = get_geolocation(ip_address)
        display_ip_results(ip_address, location)

        results["ip_address"] = ip_address
        results["geolocation"] = location
    else:
        print("[!] Could not resolve IP address.")

        results["ip_address"] = None
        results["geolocation"] = None

    # HTTP Response Headers Reconnaissance
    print("\n[+] Starting HTTP response headers reconnaissance...")

    http_results = get_http_headers(target)
    display_http_results(http_results)
    results["http"] = http_results

    # SSL/TLS Reconnaissance
    print("\n[+] Starting SSL/TLS reconnaissance...")

    ssl_results = get_ssl_certificate(target)
    display_ssl_results(ssl_results)
    results["ssl"] = ssl_results

    # Technology Detection
    print("\n[+] Starting technology detection reconnaissance...")

    tech_results = get_technologies(target)
    display_tech_results(tech_results)
    results["technology"] = tech_results

    # Subdomain Reconnaissance
    print("\n[+] Starting subdomain reconnaissance...")

    subdomains = get_subdomains(target)
    display_subdomain_results(subdomains)
    results["subdomains"] = subdomains

    # Robots.txt Reconnaissance
    print("\n[+] Starting robots.txt reconnaissance...")

    robots_results = get_robots(target)
    display_robots_results(robots_results)
    results["robots"] = robots_results

    # Generate Report
    print("\n[+] Generating reconnaissance report...")

    report_file = generate_report(target, results)

    print(f"[+] Reconnaissance report generated: {report_file}")
    print("\n[+] Reconnaissance completed successfully.")


if __name__ == "__main__":
    main()
