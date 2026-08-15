import dns.resolver


def get_a_records(target):
    records = []

    try:
        answers = dns.resolver.resolve(target, "A")

        for answer in answers:
            records.append(answer.to_text())

    except Exception as error:
        print(f"[!] A record lookup failed: {error}")

    return records


if __name__ == "__main__":
    target = "example.com"

    print(f"[*] DNS reconnaissance for: {target}")

    a_records = get_a_records(target)

    print("\nA Records:")

    for record in a_records:
        print(f" - {record}")
