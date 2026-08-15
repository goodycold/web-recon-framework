import sys
import whois


def run_whois_recon(target):
    print(f"[*] WHOIS reconnaissance for: {target}")

    try:
        result = whois.whois(target)
        return result

    except Exception as error:
        print(f"[!] WHOIS lookup failed: {error}")
        return None


def display_results(result):
    print("\n========== WHOIS RESULTS ==========")

    if result is None:
        print("No WHOIS information available.")
        return

    fields = [
        ("Domain Name", "domain_name"),
        ("Registrar", "registrar"),
        ("Creation Date", "creation_date"),
        ("Expiration Date", "expiration_date"),
        ("Name Servers", "name_servers"),
    ]

    for label, field in fields:
        value = result.get(field)

        if value:
            print(f"\n{label}:")
            print(value)
        else:
            print(f"\n{label}:")
            print("Not available")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/whois_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    result = run_whois_recon(target)
    display_results(result)


if __name__ == "__main__":
    main()
