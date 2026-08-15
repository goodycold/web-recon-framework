import sys
import requests


def get_technologies(target):
    url = f"https://{target}"

    print(f"[*] Technology reconnaissance for: {target}")
    print(f"[*] Requesting: {url}")

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "Web-Recon-Automation-Framework/1.0"
            }
        )

        technologies = {}

        server = response.headers.get("Server")
        powered_by = response.headers.get("X-Powered-By")

        if server:
            technologies["Server"] = server

        if powered_by:
            technologies["X-Powered-By"] = powered_by

        content_type = response.headers.get("Content-Type")

        if content_type:
            technologies["Content-Type"] = content_type

        return {
            "final_url": response.url,
            "status_code": response.status_code,
            "technologies": technologies
        }

    except requests.RequestException as error:
        print(f"[!] HTTP request failed: {error}")
        return None


def display_results(results):
    print("\n========== TECHNOLOGY RESULTS ==========")

    if not results:
        print("Technology information unavailable.")
        return

    print("\nFinal URL:")
    print(results["final_url"])

    print("\nStatus Code:")
    print(results["status_code"])

    print("\nDetected Technologies:")

    technologies = results["technologies"]

    if not technologies:
        print("- No technology indicators found.")
        return

    for name, value in technologies.items():
        print(f"- {name}: {value}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/tech_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    results = get_technologies(target)
    display_results(results)


if __name__ == "__main__":
    main()
