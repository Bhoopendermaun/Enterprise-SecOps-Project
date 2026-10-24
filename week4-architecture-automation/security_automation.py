#!/usr/bin/env python3
"""
Enterprise Security Automation & Incident Response Script
Author: Enterprise SecOps Team
Description: Automated IOC enrichment, log parsing, and containment action simulator.
"""

import sys
import os

# Sample Threat Intelligence Watchlists
SUSPICIOUS_IPS = ["185.220.101.5", "198.51.100.44", "45.33.22.11"]
SUSPICIOUS_HASHES = ["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"]

def analyze_log_file(filepath):
    print(f"[*] Analyzing log file: {filepath}")
    if not os.path.exists(filepath):
        print(f"[-] Error: File {filepath} not found.")
        return

    matches = 0
    with open(filepath, 'r') as f:
        for line_num, line in enumerate(f, 1):
            for ip in SUSPICIOUS_IPS:
                if ip in line:
                    print(f"[!] ALERT [Line {line_num}]: Detected malicious IP match -> {ip}")
                    matches += 1
            for hsh in SUSPICIOUS_HASHES:
                if hsh in line:
                    print(f"[!] ALERT [Line {line_num}]: Detected malicious Hash match -> {hsh}")
                    matches += 1

    print(f"[*] Analysis complete. Total indicators matched: {matches}")

if __name__ == "__main__":
    print("=== Enterprise SecOps Automation Engine ===")
    if len(sys.argv) > 1:
        analyze_log_file(sys.argv[1])
    else:
        print("[*] No log file specified. Running self-test simulation...")
        sample_log = "2026-10-18 13:00:00 INFO Connection established from 185.220.101.5 on port 443"
        print(f"[*] Simulation log line: {sample_log}")
        if any(ip in sample_log for ip in SUSPICIOUS_IPS):
            print("[!] MATCH FOUND: Automated firewall block triggered for IP 185.220.101.5.")
