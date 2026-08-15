import sys
import requests


def get_robots(target):
    print(f"[*] Robots.txt reconnaissance for: {target}")

    url = f"https://{target}/robots.txt"

    print(f"[*] Requesting: {url}")

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Web-Recon-Automation-Framework/1.0"
            }
        )

        return {
            "url": response.url,
            "status_code": response.status_code,
            "content": response.text,
        }

    except requests.RequestException as error:
        print(f"[!] Robots.txt request failed: {error}")
        return None


def display_results(results):
    print("\n========== ROBOTS.TXT RESULTS ==========")

    if results is None:
        print("Robots.txt retrieval failed.")
        return

    print("\nURL:")
    print(results["url"])

    print("\nStatus Code:")
    print(results["status_code"])

    if results["status_code"] == 404:
        print("\nRobots.txt:")
        print("Not found.")
        return

    print("\nRobots.txt Content:")

    content = results["content"].strip()

    if content:
        print(content)
    else:
        print("Empty robots.txt file.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/robots_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    results = get_robots(target)
    display_results(results)


if __name__ == "__main__":
    main()
