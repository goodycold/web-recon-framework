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

In Progress

### First Component

Implemented A-record lookup using the `dnspython` library.

### Test Command

```bash
python3 modules/dns_recon.py



test result 

[*] DNS reconnaissance for: example.com

A Records:
- 172.66.147.243
- 104.20.23.154
