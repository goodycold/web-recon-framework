# Web Recon Automation Framework — Development Notes

## Target Input Module

### Status

Completed

### Test Command

python3 recon.py example.com

### Test Result

Web Recon Automation Framework
------------------------------
Target: example.com

### Conclusion

The framework successfully accepts a target domain from the command line
and displays the supplied target.


## DNS Reconnaissance Module

### Status

Completed

### Objective

Collect publicly available DNS information for the target domain.

### DNS Records Collected

- A
- AAAA
- MX
- NS
- TXT
- CNAME

### Library

dnspython

### Implementation

The module uses a reusable `get_dns_records()` function that accepts the
target domain and DNS record type.

The `run_dns_recon()` function queries all required DNS record types and
stores the results.

The `display_results()` function presents the collected information in a
structured format.

### Test Command

python3 modules/dns_recon.py

### Test Target

example.com

### Test Result

The module successfully queried A, AAAA, MX, NS, TXT, and CNAME records.

A Records:

- 172.66.147.243
- 104.20.23.154

AAAA Records:

- 2606:4700:10::ac42:93f3
- 2606:4700:10::6814:179a

MX Records:

- 0 .

NS Records:

- hera.ns.cloudflare.com.
- elliott.ns.cloudflare.com.

TXT Records:

- "v=spf1 -all"
- "_k2n1y4vw3qtb4skdx9e7dxt97qrmmq9"

CNAME:

- No CNAME record found.

### Error Handling

The module handles:

- Missing DNS records
- Non-existent domains
- DNS timeouts
- Unexpected DNS lookup errors

The framework continues running instead of crashing when a DNS lookup
fails.

### Design

DNS functionality is separated into its own module instead of being
placed directly inside `recon.py`.

This keeps each component focused on one responsibility and makes the
framework easier to maintain, test, and extend.


