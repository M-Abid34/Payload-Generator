import argparse
from modules import xss, sqli, cmdi
from utils import encoder, obfuscator
import json
import pyperclip  # optional, for clipboard copy

def main():
    parser = argparse.ArgumentParser(description="Modular Payload Generator Tool")
    parser.add_argument('--xss', action='store_true')
    parser.add_argument('--sqli', action='store_true')
    parser.add_argument('--cmdi', action='store_true')
    parser.add_argument('--encode', choices=['base64', 'url', 'hex', 'unicode'])
    parser.add_argument('--obfuscate', action='store_true')
    parser.add_argument('--output', choices=['cli', 'json', 'clipboard'], default='cli')
    
    args = parser.parse_args()
    payloads = []

    if args.xss:
        payloads += xss.generate_payloads()

    if args.sqli:
        payloads += sqli.generate_payloads()

    if args.cmdi:
        payloads += cmdi.generate_payloads()

    if args.obfuscate:
        payloads = [obfuscator.obfuscate(p) for p in payloads]

    if args.encode:
        payloads = [encoder.encode(p, args.encode) for p in payloads]

    if args.output == 'cli':
        for p in payloads:
            print(p)
    elif args.output == 'json':
        print(json.dumps(payloads, indent=2))
    elif args.output == 'clipboard':
        pyperclip.copy('\n'.join(payloads))
        print("[+] Payloads copied to clipboard.")

if __name__ == "__main__":
    main()