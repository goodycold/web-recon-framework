# Web Recon Automation Framework

A modular Python-based web reconnaissance framework designed to automate the collection of publicly available information about a target domain.

## Features

The framework currently performs:

* DNS reconnaissance

  * A records
  * AAAA records
  * MX records
  * NS records
  * TXT records
  * CNAME records
* WHOIS reconnaissance

  * Domain name
  * Registrar
  * Creation date
  * Expiration date
  * Name servers
* IP address and geolocation reconnaissance
* HTTP response header reconnaissance
* SSL/TLS certificate reconnaissance
* Technology detection
* Subdomain reconnaissance using Certificate Transparency logs
* robots.txt reconnaissance

## Project Structure

```text
web-recon-framework/
├── recon.py
├── requirements.txt
├── PROJECT_NOTES.md
├── README.md
├── .gitignore
└── modules/
    ├── __init__.py
    ├── dns_recon.py
    ├── whois_recon.py
    ├── ip_recon.py
    ├── http_recon.py
    ├── ssl_recon.py
    ├── tech_recon.py
    ├── subdomain_recon.py
    └── robots_recon.py
```

## Requirements

* Python 3
* pip
* Internet connectivity for external reconnaissance services
* Python dependencies listed in `requirements.txt`

## Installation

Clone the repository and enter the project directory:

```bash
git clone (<REPOSITORY_URL>)
cd web-recon-framework
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the complete reconnaissance framework with:

```bash
python3 recon.py (<DOMAIN>)
```

Example:

```bash
python3 recon.py example.com
```

The framework executes the reconnaissance modules sequentially and displays the collected results.

## Individual Modules

Each reconnaissance component can also be tested independently.

Examples:

```bash
python3 modules/dns_recon.py example.com
python3 modules/whois_recon.py example.com
python3 modules/ip_recon.py example.com
python3 modules/http_recon.py example.com
python3 modules/ssl_recon.py example.com
python3 modules/tech_recon.py example.com
python3 modules/subdomain_recon.py example.com
python3 modules/robots_recon.py example.com
```

## Error Handling

The framework is designed to continue execution when an individual reconnaissance operation fails.

Examples include:

* DNS lookup failures
* Missing DNS records
* WHOIS lookup failures
* IP resolution failures
* HTTP request failures
* SSL/TLS connection failures
* Certificate Transparency service failures
* Missing robots.txt files

## Development

Each reconnaissance capability is implemented as a separate module.

This modular structure makes the framework easier to:

* Test
* Maintain
* Extend
* Debug
* Integrate into the main framework

The main `recon.py` file acts as the framework entry point and coordinates the individual modules.

## Testing

The framework has been tested using:

```bash
python3 recon.py example.com
```

Individual modules were also tested separately during development.

## Legal and Ethical Use

This framework is intended for authorized security testing, educational laboratories, CTF environments, and reconnaissance of systems for which you have permission to perform testing.

Only use the framework against domains and systems you are authorized to assess.
