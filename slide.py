import argparse
from modules import xss, sqli, cmdi
from utils import encoder, obfuscator
import json
import pyperclip

def main():
    parser = argparse.ArgumentParser(description="Modular Payload Generator Tool")
    parser.add_argument('--xss', choices=["reflected", "stored", "Dom"], help="Generate XSS Payloads")
    parser.add_argument('--sqli', choices=['error', 'union', 'blind'], help='Type of SQL injection payload to generate')
    parser.add_argument('--cmdi', action='store_true')
    parser.add_argument('--encode', choices=['base64', 'url', 'hex', 'unicode'])
    parser.add_argument('--obfuscate', action='store_true')
    parser.add_argument('--output', choices=['cli', 'json', 'clipboard'], default='cli')
    parser.add_argument('--appendfile', action='store_true', help="Append payloads to 'output.txt'")

    args = parser.parse_args()
    payloads = []

    if args.xss: 
        xss_gen = xss.XSSPayloadGenerator()
        xss_payloads = xss_gen.generate(args.xss, args.encode, args.obfuscate)
        payloads += xss_payloads

        if args.appendfile:
            with open('xss_payload.txt','a') as f:
                for p in payloads:
                    f.write(p + '\n')

    if args.sqli == 'error':
        raw_payloads = sqli.error_based_sqli()

        if args.encode:
            encoded_pairs = [(p, encoder.encode(p, args.encode)) for p in raw_payloads]
        else:
            encoded_pairs = [(p, p) for p in raw_payloads]

        if args.appendfile:
            with open('sqli_payload.txt', 'a') as f:
                for original, encoded in encoded_pairs:
                    if args.encode:
                        f.write(f"{original}<=======================>{encoded}\n\n")
                    else:
                        f.write(original + '\n')
                        

        payloads += [encoded for _, encoded in encoded_pairs]
    elif args.sqli == 'union':
        raw_payloads = sqli.union_based_sqli()
        if args.encode:
            encoded_pairs = [(p, encoder.encode(p, args.encode)) for p in raw_payloads]
        else:
            encoded_pairs = [(p, p) for p in raw_payloads]

        if args.appendfile:
            with open('sqli_payload.txt', 'a') as f:
                for original, encoded in encoded_pairs:
                    if args.encode:
                        f.write(f"{original}<=======================>{encoded}\n\n")
                    else:
                        f.write(original + '\n')
        payloads += [encoded for _, encoded in encoded_pairs]

    elif args.sqli == 'blind':
        raw_payloads = sqli.blind_sqli()
        if args.encode:
            encoded_pairs = [(p, encoder.encode(p, args.encode)) for p in raw_payloads]
        else:
            encoded_pairs = [(p, p) for p in raw_payloads]

        if args.appendfile:
            with open('sqli_payload.txt', 'a') as f:
                for original, encoded in encoded_pairs:
                    if args.encode:
                        f.write(f"{original}<=======================>{encoded}\n\n")
                    else:
                        f.write(original + '\n')

        payloads += [encoded for _, encoded in encoded_pairs]
    if args.cmdi:
        payloads += cmdi.generate_payloads()

    if args.obfuscate:
        payloads = [obfuscator.obfuscate(p) for p in payloads]

    if args.output == 'cli':
        for p in payloads:
            print(p)
    elif args.output == 'json':
        print(json.dumps(payloads, indent=2))
    elif args.output == 'clipboard':
        pyperclip.copy('\n'.join(payloads))
        print("=> Payloads copied to clipboard.")

if __name__ == "__main__":
    main()
