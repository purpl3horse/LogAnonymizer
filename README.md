# Log Anonymizer

The **Log Anonymizer** is a Python tool designed to anonymize log files before sharing them with external companies or support desks. It replaces sensitive IP addresses and hostnames with random values, ensuring that private information is obscured without compromising the structure of the logs.

## Features

- **IP Address Anonymization:** Automatically detects and replaces IPv4 addresses with random private IP addresses.
- **Hostname Anonymization:** Identifies hostnames within logs and substitutes them with randomly generated hostnames.
- **Batch Processing:** Recursively processes all `.log` and `.xml` files in the current directory.
- **Mapping Consistency:** Maintains a mapping for each original IP and hostname to ensure consistent replacements throughout a file.
- **Summary Report:** Prints a summary detailing the number of files processed, unique replacements, and total replacements made.

## Getting Started

### Prerequisites

- **Python 3.6+** is required.
- Ensure that you have the necessary permissions to read and write files in the directory containing your logs.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/log-anonymizer.git
   cd log-anonymizer
   ```

2. **Usage**

  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows, use: venv\Scripts\activate
  ```

How It Works

- **IP Replacement**: Uses a regular expression to identify IPv4 addresses and generates random private IPs from commonly used ranges (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16).
- **Hostname Replacement**: Identifies hostnames via a pattern match and replaces them with randomly generated alphanumeric strings.
- **Consistency**: Keeps a mapping of original values to their anonymized counterparts, ensuring consistency across the log file.



