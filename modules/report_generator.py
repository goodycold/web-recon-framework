from datetime import datetime
from pathlib import Path
import html


def esc(value):
    """Convert a value to HTML-safe text."""
    if value is None:
        return "Not available"

    return html.escape(str(value))


def render_value(value):
    """Render reconnaissance data in a readable HTML format."""

    if value is None:
        return "<span class='muted'>Not available</span>"

    if isinstance(value, dict):
        rows = ""

        for key, item in value.items():
            key_name = str(key).replace("_", " ").title()

            if isinstance(item, (dict, list, tuple, set)):
                item_html = render_value(item)
            else:
                item_html = esc(item)

            rows += f"""
            <tr>
                <th>{esc(key_name)}</th>
                <td>{item_html}</td>
            </tr>
            """

        return f"""
        <table>
            <tbody>
                {rows}
            </tbody>
        </table>
        """

    if isinstance(value, (list, tuple, set)):
        if not value:
            return "<span class='muted'>None found</span>"

        items = ""

        for item in value:
            items += f"<li>{esc(item)}</li>"

        return f"<ul>{items}</ul>"

    return esc(value)


def create_section(number, title, data):
    """Create a formatted reconnaissance section."""

    return f"""
    <section>
        <h2>{number}. {esc(title)}</h2>
        {render_value(data)}
    </section>
    """


def generate_report(target, results):
    """
    Generate a professional client-style HTML reconnaissance report.
    """

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    now = datetime.now()

    generated_time = now.strftime("%Y-%m-%d %H:%M:%S")
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    safe_target = (
        target
        .replace("/", "_")
        .replace(":", "_")
        .replace("\\", "_")
    )

    report_file = reports_dir / f"{safe_target}_recon_{timestamp}.html"

    # Retrieve collected reconnaissance results
    dns_results = results.get("dns")
    whois_results = results.get("whois")
    ip_address = results.get("ip_address")
    geolocation = results.get("geolocation")
    http_results = results.get("http")
    ssl_results = results.get("ssl")
    technology = results.get("technology")
    subdomains = results.get("subdomains")
    robots = results.get("robots")

    # Build IP/geolocation data
    ip_results = {
        "IP Address": ip_address,
        "Geolocation": geolocation
    }

    html_report = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>
Web Reconnaissance Report - {esc(target)}
</title>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 0;
    background: #f4f6f8;
    color: #202124;
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
}}

.container {{
    max-width: 1150px;
    margin: 40px auto;
    background: #ffffff;
    padding: 45px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}}

header {{
    border-bottom: 3px solid #1f2937;
    padding-bottom: 25px;
    margin-bottom: 35px;
}}

h1 {{
    margin: 0 0 10px 0;
    font-size: 32px;
}}

h2 {{
    margin-top: 45px;
    padding-bottom: 10px;
    border-bottom: 2px solid #e5e7eb;
    color: #111827;
}}

h3 {{
    margin-top: 25px;
}}

.metadata {{
    margin-top: 25px;
    padding: 18px;
    background: #f8fafc;
    border-left: 4px solid #374151;
}}

.metadata p {{
    margin: 5px 0;
}}

.summary {{
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    padding: 25px;
    margin-top: 20px;
}}

.observation {{
    background: #f9fafb;
    border-left: 4px solid #6b7280;
    padding: 15px 20px;
    margin: 12px 0;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}

th,
td {{
    border: 1px solid #e5e7eb;
    padding: 12px 15px;
    text-align: left;
    vertical-align: top;
}}

th {{
    width: 30%;
    background: #f8fafc;
    font-weight: 600;
}}

tr:nth-child(even) td {{
    background: #fcfcfd;
}}

ul {{
    padding-left: 25px;
}}

li {{
    margin-bottom: 6px;
}}

.muted {{
    color: #6b7280;
    font-style: italic;
}}

.code {{
    font-family: monospace;
    background: #f3f4f6;
    padding: 3px 6px;
    border-radius: 4px;
}}

footer {{
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #d1d5db;
    color: #6b7280;
    font-size: 13px;
}}

@media print {{

    body {{
        background: white;
    }}

    .container {{
        margin: 0;
        box-shadow: none;
        max-width: none;
    }}

    section {{
        break-inside: avoid;
    }}

}}

</style>

</head>

<body>

<div class="container">

<header>

<h1>Web Reconnaissance Report</h1>

<p>
<strong>Target:</strong>
{esc(target)}
</p>

<div class="metadata">

<p>
<strong>Assessment Type:</strong>
Passive Web Reconnaissance
</p>

<p>
<strong>Generated:</strong>
{esc(generated_time)}
</p>

</div>

</header>


<section>

<h2>1. Executive Summary</h2>

<div class="summary">

<p>
This report presents publicly available reconnaissance information
collected for the target domain
<strong>{esc(target)}</strong>.
</p>

<p>
The reconnaissance framework collected information relating to
DNS records, domain registration, IP address and geolocation,
HTTP responses, SSL/TLS certificates, technology indicators,
publicly known subdomains, and web resources.
</p>

<p>
The results provide an initial external view of the target's
publicly observable infrastructure and web-facing characteristics.
</p>

</div>

</section>


<section>

<h2>2. Target Information</h2>

<table>

<tr>
<th>Target</th>
<td>{esc(target)}</td>
</tr>

<tr>
<th>Assessment Type</th>
<td>Passive Web Reconnaissance</td>
</tr>

<tr>
<th>Generated</th>
<td>{esc(generated_time)}</td>
</tr>

</table>

</section>


{create_section(3, "DNS Reconnaissance", dns_results)}


{create_section(4, "WHOIS Information", whois_results)}


{create_section(5, "IP Address & Geolocation", ip_results)}


{create_section(6, "HTTP Response Information", http_results)}


{create_section(7, "SSL/TLS Information", ssl_results)}


{create_section(8, "Technology Detection", technology)}


{create_section(9, "Subdomain Enumeration", subdomains)}


{create_section(10, "robots.txt", robots)}


<section>

<h2>11. Key Observations</h2>

<div class="observation">
The target domain resolves to publicly accessible IPv4 and IPv6
addresses.
</div>

<div class="observation">
The DNS infrastructure indicates the use of publicly identifiable
name servers.
</div>

<div class="observation">
The HTTP response exposes publicly observable server and content
information.
</div>

<div class="observation">
The target supports TLS encryption and exposes certificate
information through the TLS service.
</div>

<div class="observation">
Certificate Transparency data may reveal publicly known
subdomains associated with the target.
</div>

<div class="observation">
The reconnaissance results represent publicly observable
information and should not be interpreted as confirmed
security vulnerabilities.
</div>

</section>


<section>

<h2>12. Methodology</h2>

<div class="summary">

<p>
The framework performed passive reconnaissance using publicly
accessible information sources and standard network protocols.
</p>

<ul>

<li>DNS record enumeration</li>

<li>WHOIS domain registration lookup</li>

<li>IPv4 resolution and basic geolocation</li>

<li>HTTP response inspection</li>

<li>SSL/TLS certificate inspection</li>

<li>Technology indicator detection</li>

<li>Certificate Transparency subdomain enumeration</li>

<li>robots.txt retrieval</li>

</ul>

<p>
No exploitation or intrusive vulnerability testing is performed
by these reconnaissance modules.
</p>

</div>

</section>


<section>

<h2>13. Limitations</h2>

<ul>

<li>
The report contains information that was publicly accessible
during the reconnaissance process.
</li>

<li>
Results may change over time as DNS records, certificates,
web infrastructure, and other public information change.
</li>

<li>
Geolocation information may represent hosting infrastructure
rather than the physical location of the organization.
</li>

<li>
Technology detection is based on publicly exposed indicators
and may not identify all technologies in use.
</li>

<li>
Certificate Transparency enumeration does not guarantee that
all active subdomains have been discovered.
</li>

<li>
The presence of information in this report does not by itself
indicate a security vulnerability.
</li>

</ul>

</section>


<footer>

<strong>Web Recon Automation Framework</strong><br>

Generated automatically from reconnaissance module results.<br>

This report is intended for authorized reconnaissance and
security assessment activities.

</footer>


</div>

</body>

</html>
"""

    report_file.write_text(html_report, encoding="utf-8")

    return report_file
