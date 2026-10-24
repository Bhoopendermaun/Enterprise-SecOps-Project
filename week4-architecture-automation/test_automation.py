#!/usr/bin/env python3
"""
Unit Test Suite for Enterprise Security Automation Engine
Author: Enterprise SecOps Team
Description: Validates IOC detection accuracy against mock log files.
"""

import unittest
import os
import tempfile

# Import the functions from our security automation script
from security_automation import SUSPICIOUS_IPS, SUSPICIOUS_HASHES

class TestSecOpsAutomation(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary log file for testing."""
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        # Write a mix of clean and malicious log lines
        self.test_file.write("2026-10-18 10:00:00 INFO User login successful from 192.168.1.50\n")
        self.test_file.write("2026-10-18 10:05:22 WARN Outbound transfer to suspicious IP 185.220.101.5\n")
        self.test_file.write("2026-10-18 10:10:15 ERROR File execution detected hash e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n")
        self.test_file.write("2026-10-18 10:15:00 INFO Normal health check ping from 10.0.0.5\n")
        self.test_file.close()

    def tearDown(self):
        """Clean up the temporary file after tests run."""
        os.unlink(self.test_file.name)

    def test_suspicious_ip_detection(self):
        """Test if known malicious IPs are successfully identified in log lines."""
        found_ips = 0
        with open(self.test_file.name, 'r') as f:
            for line in f:
                for ip in SUSPICIOUS_IPS:
                    if ip in line:
                        found_ips += 1
        self.assertEqual(found_ips, 1, "Failed to detect the exact number of malicious IP indicators.")

    def test_suspicious_hash_detection(self):
        """Test if known malicious file hashes are successfully identified."""
        found_hashes = 0
        with open(self.test_file.name, 'r') as f:
            for line in f:
                for hsh in SUSPICIOUS_HASHES:
                    if hsh in line:
                        found_hashes += 1
        self.assertEqual(found_hashes, 1, "Failed to detect the exact number of malicious hash indicators.")

if __name__ == '__main__':
    unittest.main()
