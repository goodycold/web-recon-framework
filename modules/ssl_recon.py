import socket
import ssl
import sys


def get_ssl_certificate(target):
    hostname = target.replace("https://", "").replace("http://", "").split("/")[0]

    print(f"[*] Retrieving SSL/TLS certificate for: {hostname}")

    context = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                certificate = secure_sock.getpeercert()
                tls_version = secure_sock.version()

                return {
                    "certificate": certificate,
                    "tls_version": tls_version
                }

    except (socket.timeout, socket.error, ssl.SSLError) as error:
        print(f"[!] SSL/TLS connection failed: {error}")
        return None


def format_certificate_name(name):
    if not name:
        return "Not available"

    parts = []

    for attribute_group in name:
        for attribute, value in attribute_group:
            parts.append(f"{attribute}={value}")

    return ", ".join(parts)


def display_results(results):
    if not results:
        print("[!] No SSL/TLS certificate information available.")
        return

    certificate = results["certificate"]
    tls_version = results["tls_version"]

    print("\n========== SSL/TLS CERTIFICATE RESULTS ==========\n")

    print("TLS Version:")
    print(tls_version)

    print("\nSubject:")
    print(format_certificate_name(certificate.get("subject")))

    print("\nIssuer:")
    print(format_certificate_name(certificate.get("issuer")))

    print("\nValid From:")
    print(certificate.get("notBefore", "Not available"))

    print("\nValid Until:")
    print(certificate.get("notAfter", "Not available"))

    print("\nSerial Number:")
    print(certificate.get("serialNumber", "Not available"))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 modules/ssl_recon.py (<domain>)")
        sys.exit(1)

    target = sys.argv[1]

    print(f"[*] SSL/TLS reconnaissance for: {target}")

    results = get_ssl_certificate(target)
    display_results(results)


if __name__ == "__main__":
    main()
