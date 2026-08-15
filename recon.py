import sys

if len(sys.argv) != 2:
    print("Usage: python3 recon.py (TARGET)")
    sys.exit(1)

target = sys.argv[1]

print("Web Recon Automation Framework")
print("------------------------------")
print(f"Target: {target}")
