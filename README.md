# Web Recon Automation Framework

**Author:** Spirit

A modular Python-based web reconnaissance framework for collecting publicly available information about a target domain.

The project was built to make basic web reconnaissance easier by separating each reconnaissance task into its own module and then combining the results through a single main script.

---

## Features

The framework currently performs the following reconnaissance tasks:

### DNS Reconnaissance

Collects:

* A records
* AAAA records
* MX records
* NS records
* TXT records
* CNAME records

### WHOIS Reconnaissance

Collects available domain registration information, including:

* Domain name
* Registrar
* Creation date
* Expiration date
* Name servers
* WHOIS server
* Domain status
* DNSSEC information

### IP Address & Geolocation

Resolves the target domain to an IP address and retrieves basic geolocation information.

The results can include:

* IP address
* Country
* Region
* City
* Organization
* Timezone
* ASN information when provided by the service

### HTTP Reconnaissance

Connects to the target over HTTPS and collects:

* Final URL
* HTTP status code
* Response headers
* Server information
* Content type
* Cache-related headers
* Other publicly exposed HTTP information

### SSL/TLS Reconnaissance

Collects information from the target's TLS certificate, including:

* TLS version
* Certificate subject
* Certificate issuer
* Certificate version
* Serial number
* Validity dates
* Subject Alternative Names
* OCSP information
* CA issuer information
* CRL distribution points

### Technology Detection

Checks publicly visible HTTP information for technology indicators such as:

* Web server
* Content type
* Other headers that may identify technologies

### Subdomain Reconnaissance

Uses Certificate Transparency logs to identify publicly known subdomains associated with the target.

### robots.txt Reconnaissance

Requests:

```text
https://(<DOMAIN>)/robots.txt
```

and records:

* URL
* HTTP status code
* Returned content

### Automatic Report Generation

After reconnaissance is completed, the framework automatically generates an HTML report.

Reports are stored in:

```text
reports/
```

Example:

```text
reports/example.com_recon_2026-08-16_09-19-35.html
```

The generated report contains:

1. Executive Summary
2. Target Information
3. DNS Reconnaissance
4. WHOIS Information
5. IP Address & Geolocation
6. HTTP Response Information
7. SSL/TLS Information
8. Technology Detection
9. Subdomain Enumeration
10. robots.txt
11. Key Observations
12. Methodology
13. Limitations

---

# Project Structure

```text
web-recon-framework/
│
├── recon.py
├── requirements.txt
├── README.md
├── PROJECT_NOTES.md
├── .gitignore
│
├── modules/
│   ├── __init__.py
│   ├── dns_recon.py
│   ├── whois_recon.py
│   ├── ip_recon.py
│   ├── http_recon.py
│   ├── ssl_recon.py
│   ├── tech_recon.py
│   ├── subdomain_recon.py
│   ├── robots_recon.py
│   └── report_generator.py
│
└── reports/
    └── generated HTML reports
```

---

# Requirements

The framework requires:

* Python 3
* pip
* Internet connectivity
* A Python virtual environment
* The packages listed in `requirements.txt`

The external services used by the modules must also be reachable from the system running the framework.

---

# Installation

Clone the project:

```bash
git clone (<REPOSITORY_URL>)
```

Enter the project directory:

```bash
cd web-recon-framework
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the complete framework:

```bash
python3 recon.py (<DOMAIN>)
```

Example:

```bash
python3 recon.py example.com
```

The framework runs each reconnaissance module and displays the results in the terminal.

After the modules finish, an HTML reconnaissance report is automatically generated in the `reports/` directory.

Example output:

```text
[+] Generating reconnaissance report...
[+] Reconnaissance report generated:
reports/example.com_recon_2026-08-16_09-19-35.html

[+] Reconnaissance completed successfully.
```

---

# Opening a Report

After running the framework, list the generated reports:

```bash
ls -lt reports/
```

To open the latest report using the default browser:

```bash
xdg-open "$(find reports -maxdepth 1 -type f -name '*.html' -printf '%T@ %p\n' | sort -nr | head -1 | cut -d' ' -f2-)"
```

Alternatively, open a specific report:

```bash
xdg-open reports/(<REPORT_FILE>).html
```

---

# Running Individual Modules

Each module can also be tested separately.

### DNS

```bash
python3 modules/dns_recon.py example.com
```

### WHOIS

```bash
python3 modules/whois_recon.py example.com
```

### IP Reconnaissance

```bash
python3 modules/ip_recon.py example.com
```

### HTTP

```bash
python3 modules/http_recon.py example.com
```

### SSL/TLS

```bash
python3 modules/ssl_recon.py example.com
```

### Technology Detection

```bash
python3 modules/tech_recon.py example.com
```

### Subdomains

```bash
python3 modules/subdomain_recon.py example.com
```

### robots.txt

```bash
python3 modules/robots_recon.py example.com
```

---

# How the Framework Works

The main entry point is:

```text
recon.py
```

The main script accepts a domain as an argument and then calls each reconnaissance module.

The general workflow is:

```text
Target Domain
      │
      ▼
   recon.py
      │
      ├── DNS Recon
      │
      ├── WHOIS Recon
      │
      ├── IP & Geolocation
      │
      ├── HTTP Recon
      │
      ├── SSL/TLS Recon
      │
      ├── Technology Detection
      │
      ├── Subdomain Recon
      │
      └── robots.txt Recon
              │
              ▼
       Collected Results
              │
              ▼
       Report Generator
              │
              ▼
        HTML Report
```

---

# Architecture

The project uses a modular structure.

Instead of putting every reconnaissance function inside one large Python file, each capability is separated into its own module.

For example:

```text
dns_recon.py
whois_recon.py
ip_recon.py
http_recon.py
ssl_recon.py
tech_recon.py
subdomain_recon.py
robots_recon.py
```

Each module is responsible for one type of reconnaissance.

The `recon.py` script acts as the main controller. It calls the modules, collects their results, and passes those results to:

```text
modules/report_generator.py
```

The report generator converts the collected information into a structured HTML report.

This structure makes it easier to add another reconnaissance module later without having to rewrite the whole framework.

For example, a future module could be added as:

```text
modules/sitemap_recon.py
```

and then connected to the main framework.

---

# Libraries and External Services

The project uses Python libraries for the individual reconnaissance tasks.

Depending on the module, the framework uses libraries such as:

* `requests` for HTTP requests and external web APIs
* `dnspython` for DNS queries
* `python-whois` for WHOIS information
* Python's built-in `ssl` module for TLS certificate information
* Python's built-in `socket` module for hostname resolution
* `datetime` for report timestamps
* `pathlib` for file and directory handling
* `html` for safely formatting report content

The subdomain module uses Certificate Transparency data from:

```text
crt.sh
```

The IP geolocation module uses an external IP geolocation service.

The exact Python dependencies are listed in:

```text
requirements.txt
```

---

# Error Handling

The framework attempts to handle failures inside individual reconnaissance modules.

Possible problems include:

* DNS lookup failures
* DNS records not being available
* WHOIS lookup failures
* Domain resolution failures
* HTTP connection failures
* SSL/TLS connection failures
* Certificate Transparency service failures
* `robots.txt` returning a 404
* External API availability problems
* Network timeouts

For example, Certificate Transparency may occasionally be unavailable or slow.

This does not necessarily mean that the target has no subdomains.

It may simply mean that the external service could not be reached at that time.

---

# Limitations

This framework is intended for basic reconnaissance and has several limitations.

### DNS

DNS records can change over time, and the results represent the records available at the time of the scan.

### WHOIS

Some domains provide limited registration information or privacy-protected information.

### Geolocation

IP geolocation identifies hosting or network infrastructure and should not automatically be treated as the physical location of an organization.

### Technology Detection

Technology detection is based mainly on publicly exposed indicators and may not identify every technology running behind the target.

### Subdomain Enumeration

Certificate Transparency enumeration does not guarantee that every active subdomain will be discovered.

### External Services

Some modules depend on external services. Service outages, rate limits, network problems, or timeouts can affect the results.

### Passive Reconnaissance

The framework is designed around publicly accessible information and does not perform exploitation or intrusive vulnerability testing.

The information collected should therefore not automatically be considered evidence of a security vulnerability.

---

# Testing

The complete framework was tested with:

```bash
python3 recon.py example.com
```

The individual modules were also tested independently during development.

The framework successfully generated HTML reports in the:

```text
reports/
```

directory.

---

# Output

A successful run produces an HTML report similar to:

```text
reports/
└── example.com_recon_2026-08-16_09-19-35.html
```

The report is intended to provide a readable summary of the reconnaissance results that can be reviewed before a security assessment.

---

# Legal and Ethical Use

This project is intended for:

* Authorized penetration testing
* Security assessments
* Educational projects
* CTF environments
* Personal laboratories
* Systems for which permission has been obtained

Only use this framework against domains and systems that you are authorized to assess.

The author is not responsible for unauthorized or illegal use of this tool.

---

# Author

**Spirit**

Web Recon Automation Framework

