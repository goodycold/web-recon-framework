import sys
import requests


def get_subdomains(target):
    print(f"[*] Subdomain reconnaissance for: {target}")
    print("[*] Querying Certificate Transparency logs...")

    url = f"https://crt.sh/?q=%25.{target}&output=json"

    headers = {
        "User-Agent": "Web-Recon-Automation-Framework/1.0"
    }

    try:
        response = requests.get(
            url,
            timeout=60,
            headers=headers
        )

        response.raise_for_status()

        records = response.json()
        subdomains = set()

        for record in records:
            names = record.get("name_value", "")

            for name in names.splitlines():
                name = name.strip().lower()

                if name.startswith("*."):
                    name = name[2:]

                if name == target or name.endswith(f".{target}"):
                    subdomains.add(name)

        return sorted(subdomains)

    except requests.Timeout:
        print("[!] Certificate Transparency request timed out.")
        return []

    except requests.HTTPError as error:
        print(f"[!] Certificate Transparency HTTP error: {error}")
        return []

    except requests.ConnectionError as error:
        print(f"[!] Certificate Transparency connection error: {error}")
        return []

    except requests.RequestException as error:
        print(f"[!] Certificate Transparency request failed: {error}")
        return []

    except ValueError:
        print("[!] Could not parse Certificate Transparency response.")
        return []


def display_results(subdomains):
    print("\n========== SUBDOMAIN RESULTS ==========")

    if not subdomains:
        print("No subdomains found or Certificate Transparency data unavailable.")
        return

    print(f"\nSubdomains Found: {len(subdomains)}")

    for subdomain in subdomains:
        print(f"- {subdomain}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/subdomain_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    subdomains = get_subdomains(target)
    display_results(subdomains)


if __name__ == "__main__":
    main()
