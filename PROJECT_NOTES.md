
# Web Recon Automation Framework — Development Notes

## Target Input Module


### Test Command

python3 recon.py example.com

### Test Result

Web Recon Automation Framework

Target: example.com



## DNS Reconnaissance Module

### Status

Completed


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









## WHOIS Reconnaissance Module


### Objective

Collect publicly available WHOIS information for the target domain.

### Information Collected

- Domain name
- Registrar
- Creation date
- Expiration date
- Name servers

### Library

python-whois

### Test Command

python3 modules/whois_recon.py example.com

### Test Target

example.com

### Test Result

The WHOIS module successfully retrieved publicly available registration
information.

Domain Name:

EXAMPLE.COM

Registrar:

RESERVED-Internet Assigned Numbers Authority

Creation Date:

1995-08-14 04:00:00+00:00

Expiration Date:

2027-08-13 04:00:00+00:00

Name Servers:

- ELLIOTT.NS.CLOUDFLARE.COM
- HERA.NS.CLOUDFLARE.COM

### Error Handling

The module handles WHOIS lookup failures without crashing the framework.

If WHOIS information cannot be retrieved, the module reports that the
information is unavailable.

### Design

WHOIS functionality is separated into its own module instead of being
placed directly inside `recon.py`.

This keeps the module focused on one responsibility and allows it to be
tested independently before integration with the main framework.








## IP Address & Geolocation Module


### Information Collected

- IPv4 address
- Country
- Region
- City
- Organization
- Timezone

### Libraries

- Python `socket`
- `requests`

### Implementation

The `resolve_ip()` function resolves the target domain to an IPv4
address using Python's socket library.

The `get_geolocation()` function queries the IP geolocation service
and retrieves basic location information for the resolved IP address.

The `display_results()` function presents the collected information
in a structured format.

### Test Command

python3 modules/ip_recon.py example.com

### Test Target

example.com

### Test Result

The module successfully resolved the target domain to an IP address
and retrieved basic geolocation information.

IP Address:

- 104.20.23.154

Country:

- US

Region:

- California

City:

- San Francisco

Organization:

- AS13335 Cloudflare, Inc.

Timezone:

- America/Los_Angeles

### Error Handling

The module handles:

- DNS resolution failures
- Invalid or unavailable IP addresses
- Geolocation request failures
- Network timeouts

The module reports errors and continues without crashing.

### Design

IP address and geolocation functionality is separated into its own
module instead of being placed directly inside `recon.py`.

This keeps the module focused on one responsibility and allows it to
be tested independently before integration with the main framework.



## HTTP Response Headers Reconnaissance Module


### Objective

Collect publicly available HTTP response information from the target
website.

### Information Collected

- Final URL
- HTTP status code
- HTTP response headers
- Server banner
- Content type
- Cache-related headers
- Allowed HTTP methods when disclosed

### Library

requests

### Test Command

python3 modules/http_recon.py example.com

### Test Target

example.com

### Test Result

The HTTP reconnaissance module successfully connected to the target
over HTTPS and retrieved the HTTP response information.

Final URL:

https://example.com/

Status Code:

200

Example Response Headers:

- Server: cloudflare
- Content-Type: text/html
- Transfer-Encoding: chunked
- Connection: keep-alive
- Last-Modified: Wed, 12 Aug 2026 20:15:57 GMT
- Allow: GET, HEAD
- Age: 2668
- CF-Cache-Status: HIT
- Content-Encoding: gzip

### Error Handling

The module handles:

- HTTP request failures
- Connection errors
- Request timeouts
- Invalid or unreachable targets

The module reports the error and continues instead of crashing.

### Design

HTTP functionality is separated into its own module instead of being
placed directly inside `recon.py`.

This keeps HTTP reconnaissance focused on one responsibility and allows
the module to be tested independently before integration.


## SSL/TLS Reconnaissance Module

### Status

Completed

### Objective

Collect publicly available SSL/TLS certificate information for the target
domain.

### Information Collected

- TLS version
- Certificate subject
- Certificate issuer
- Certificate validity start date
- Certificate validity expiration date
- Certificate serial number

### Library

Python standard library:
- ssl
- socket

### Test Command

python3 modules/ssl_recon.py example.com

### Test Target

example.com

### Test Result

The SSL/TLS module successfully retrieved certificate information.

TLS Version:

TLSv1.3

Subject:

commonName=example.com

Issuer:

countryName=US, organizationName=SSL Corporation, commonName=Cloudflare TLS Issuing ECC CA 3

Valid From:

Jul 29 22:10:08 2026 GMT

Valid Until:

Oct 27 22:17:21 2026 GMT

Serial Number:

0624D0AB311558780B7D5213B9631831

### Error Handling

The module handles:

- DNS resolution failures
- Connection failures
- SSL/TLS connection errors
- Certificate retrieval errors

The module reports failures without crashing the framework.

### Design

SSL/TLS functionality is separated into its own module instead of being
placed directly inside `recon.py`.

This keeps the certificate reconnaissance functionality independent,
testable, and reusable.

### Conclusion

The SSL/TLS reconnaissance module successfully retrieves basic certificate
information from the target domain and is ready for integration with the
main framework.



## Technology Detection Module


### Objective

Identify basic technology indicators exposed by the target web server.

### Information Collected

- Web server
- X-Powered-By header
- Content-Type
- Final URL
- HTTP status code

### Library

requests

### Test Command

python3 modules/tech_recon.py example.com

### Test Target

example.com

### Test Result

The Technology Detection module successfully connected to the target
and identified publicly exposed technology indicators.

Final URL:

https://example.com/

Status Code:

200

Detected Technologies:

- Server: cloudflare
- Content-Type: text/html

### Error Handling

The module handles HTTP request failures without crashing the framework.

If the target cannot be reached, the module reports that technology
information is unavailable.

### Design

Technology detection is separated into its own module instead of being
placed directly inside `recon.py`.

This keeps technology identification focused on one responsibility and
allows the module to be tested independently before integration.






## Subdomain Reconnaissance Module

### Status

Completed

### Objective

Discover publicly known subdomains associated with the target domain using
Certificate Transparency logs.

### Information Collected

- Subdomain names
- Number of discovered subdomains

### Data Source

Certificate Transparency logs provided through crt.sh.

### Library

requests

### Implementation

The module queries Certificate Transparency data for certificates
associated with the target domain.

The `get_subdomains()` function retrieves and processes the certificate
records.

Wildcard entries are normalized and duplicate subdomains are removed.

The `display_results()` function presents the discovered subdomains in a
structured format.

### Test Command

python3 modules/subdomain_recon.py example.com

### Test Target

example.com

### Test Result

The module successfully discovered publicly listed subdomains.

Subdomains Found:

- dev.example.com
- example.com
- m.example.com
- products.example.com
- support.example.com
- www.example.com

### Error Handling

The module handles:

- HTTP request failures
- Certificate Transparency response errors
- Invalid JSON responses
- Empty results

The module reports errors without crashing the framework.

### Design

Subdomain functionality is separated into its own module instead of being
placed directly inside `recon.py`.

This keeps the reconnaissance functionality modular and allows the
subdomain enumeration component to be tested independently before
integration.


## Robots.txt Reconnaissance Module

### Status

Completed

### Objective

Retrieve and analyze the target website's publicly accessible `robots.txt`
file.

### Information Collected

- Robots.txt URL
- HTTP status code
- Robots.txt contents
- Whether the file exists

### Library

requests

### Implementation

The module requests `/robots.txt` from the target domain.

The `get_robots()` function retrieves the robots.txt response and stores
the URL, HTTP status code, and response content.

The `display_results()` function presents the results in a structured
format.

### Test Command

python3 modules/robots_recon.py example.com

### Test Target

example.com

### Test Result

The module successfully requested the robots.txt file.

URL:

https://example.com/robots.txt

Status Code:

404

Result:

Robots.txt not found.

### Error Handling

The module handles:

- HTTP request failures
- Connection errors
- Request timeouts
- Missing robots.txt files
- Empty robots.txt files

The module reports errors without crashing the framework.


