import base64
import argparse

def encode_ip_to_url(ip_address):
    # Encode the IP address to Base64
    encoded_ip = base64.b64encode(ip_address.encode()).decode()
    # Create the URL
    return f"https://en.fofa.info/result?qbase64={encoded_ip}"

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ips = file.readlines()
            for ip in ips:
                ip = ip.strip()  # Remove whitespace and newline characters
                if ip:
                    url = encode_ip_to_url(ip)
                    print(f"Encoded URL for {ip}: {url}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encode IP(s) to Base64 and generate FOFA URLs.")
    parser.add_argument("ip", nargs="?", type=str, help="Single IP address to encode.")
    parser.add_argument("-i", "--input", type=str, help="Path to the file containing IP addresses.")
    args = parser.parse_args()

    if args.input:
        # Process multiple IPs from a file
        process_file(args.input)
    elif args.ip:
        # Process a single IP passed as an argument
        url = encode_ip_to_url(args.ip)
        print(f"Encoded URL for {args.ip}: {url}")
    else:
        print("Please provide either a single IP address or an input file.")
