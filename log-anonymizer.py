import re
import random
import ipaddress
import os
from pathlib import Path
import string

class LogAnonymizer:
    def __init__(self):
        self.ip_mapping = {}
        self.hostname_mapping = {}
        self.ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        self.hostname_pattern = r'\b[a-zA-Z0-9][-a-zA-Z0-9.]*[a-zA-Z0-9]\b'
        self.changes_count = {'ips': 0, 'hostnames': 0}

    def generate_random_ip(self):
        # Generate random private IP addresses
        networks = [
            '10.0.0.0/8',
            '172.16.0.0/12',
            '192.168.0.0/16'
        ]
        network = ipaddress.ip_network(random.choice(networks))
        return str(ipaddress.ip_address(random.randint(
            int(network.network_address),
            int(network.broadcast_address)
        )))

    def generate_random_hostname(self, length=8):
        # Generate random hostname
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def anonymize_ip(self, match):
        ip = match.group(0)
        if ip not in self.ip_mapping:
            self.ip_mapping[ip] = self.generate_random_ip()
            self.changes_count['ips'] += 1
        return self.ip_mapping[ip]

    def anonymize_hostname(self, match):
        hostname = match.group(0)
        if hostname not in self.hostname_mapping:
            self.hostname_mapping[hostname] = self.generate_random_hostname()
            self.changes_count['hostnames'] += 1
        return self.hostname_mapping[hostname]

    def process_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace IPs
            content = re.sub(self.ip_pattern, self.anonymize_ip, content)
            # Replace hostnames
            content = re.sub(self.hostname_pattern, self.anonymize_hostname, content)

            # Create output filename
            output_path = file_path.parent / f"{file_path.stem}_anonymized{file_path.suffix}"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return True

        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return False

def main():
    anonymizer = LogAnonymizer()
    processed_files = 0
    failed_files = 0

    # Process all .log and .xml files in current directory
    for ext in ['.log', '.xml']:
        for file_path in Path('.').glob(f'**/*{ext}'):
            print(f"Processing {file_path}...")
            if anonymizer.process_file(file_path):
                processed_files += 1
            else:
                failed_files += 1

    # Print summary
    print("\nProcessing complete!")
    print(f"Files processed successfully: {processed_files}")
    print(f"Files failed: {failed_files}")
    print(f"Unique IPs anonymized: {len(anonymizer.ip_mapping)}")
    print(f"Total IP replacements: {anonymizer.changes_count['ips']}")
    print(f"Unique hostnames anonymized: {len(anonymizer.hostname_mapping)}")
    print(f"Total hostname replacements: {anonymizer.changes_count['hostnames']}")

if __name__ == "__main__":
    main()
