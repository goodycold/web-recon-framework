import sys

from modules.dns_recon import run_dns_recon, display_results


def main():
    print("Web Recon Automation Framework")
    print("------------------------------")

    if len(sys.argv) != 2:
        print("Usage: python3 recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    print(f"Target: {target}")

    print("\n[+] Starting DNS reconnaissance...")

    dns_results = run_dns_recon(target)

    display_results(dns_results)


if __name__ == "__main__":
    main()
