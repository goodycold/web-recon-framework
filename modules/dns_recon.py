import dns.resolver


def get_dns_records(target, record_type):
    """
    Query DNS records for the target.

    Args:
        target: Domain name to query.
        record_type: DNS record type such as A, AAAA, MX, NS, TXT, or CNAME.

    Returns:
        A list containing the discovered DNS records.
    """

    records = []

    try:
        answers = dns.resolver.resolve(target, record_type)

        for answer in answers:
            records.append(answer.to_text())

    except dns.resolver.NoAnswer:
        print(f"[!] No {record_type} records found.")

    except dns.resolver.NXDOMAIN:
        print(f"[!] Domain does not exist: {target}")

    except dns.resolver.Timeout:
        print(f"[!] DNS query timed out for {record_type}.")

    except Exception as error:
        print(f"[!] {record_type} lookup failed: {error}")

    return records


def run_dns_recon(target):
    """
    Run DNS reconnaissance against the target.

    Returns:
        Dictionary containing the discovered DNS records.
    """

    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    results = {}

    print(f"[*] DNS reconnaissance for: {target}")

    for record_type in record_types:
        print(f"[*] Querying {record_type} records...")

        results[record_type] = get_dns_records(
            target,
            record_type
        )

    return results


def display_results(results):
    """
    Display DNS reconnaissance results.
    """

    print("\n========== DNS RESULTS ==========")

    for record_type, records in results.items():

        print(f"\n{record_type} Records:")

        if records:
            for record in records:
                print(f" - {record}")
        else:
            print(" - No records found.")


if __name__ == "__main__":

    target = "example.com"

    results = run_dns_recon(target)

    display_results(results)
