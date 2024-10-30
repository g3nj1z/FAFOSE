# FAFOSE 

Fast FOFA Search (FAFOSE) automates the encoding of IP addresses into FOFA-compatible Base64 URLs for quick searches on FOFA’s platform. It allows encoding of single IP addresses or a list from a specified file, outputting each encoded URL in a clear, readable format.

## Features
- Encode IP Addresses in One-Go: Converts individual or multiple IPs into Base64 format and constructs FOFA-compatible search URLs.
- Batch Processing: Reads IPs from a specified file, encoding each and displaying URLs for easy access.
- Lightweight and Efficient: Simple script leveraging Python’s base64 library.

### Prerequisites

- Ensure `tshark` (Wireshark command-line tool) is installed.

   ```
## Example

### Single Target
   ```bash
   python3 fafose.py <ip address>
   ```

### Mutiple Target
   ```bash
   python3 fafose.py -i path/ip.txt
   ```

Each IP will generate an encoded FOFA URL, displayed in the format:
Encoded URL for 192.168.1.1: https://en.fofa.info/result?qbase64=<Base64_encoded_IP>
