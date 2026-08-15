import sys
import requests


def get_http_headers(target):
    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    print(f"[*] Requesting HTTP headers from: {target}")

    try:
        response = requests.get(
            target,
            timeout=10,
            allow_redirects=True
        )

        return {
            "url": response.url,
            "status_code": response.status_code,
            "headers": dict(response.headers)
        }

    except requests.exceptions.Timeout:
        print("[!] HTTP request timed out.")
        return None

    except requests.exceptions.RequestException as error:
        print(f"[!] HTTP request failed: {error}")
        return None


def display_results(results):
    if not results:
        print("[!] No HTTP results available.")
        return

    print("\n========== HTTP RESPONSE RESULTS ==========\n")

    print("Final URL:")
    print(results["url"])

    print("\nStatus Code:")
    print(results["status_code"])

    print("\nHTTP Response Headers:")

    for name, value in results["headers"].items():
        print(f"- {name}: {value}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/http_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    print(f"[*] HTTP reconnaissance for: {target}")

    results = get_http_headers(target)
    display_results(results)


if __name__ == "__main__":
    main()
