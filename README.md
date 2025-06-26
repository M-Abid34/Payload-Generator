
Presnt you all A modular , fast and easy to use Payload Generator that generates all type of payloads at a single place.
The best thing is it is easy to use and customise able and comes with an inbuilt GUI in Flask.       
         
             ______      ___ ____  _____  
            / ____| |   |_ _|  _ \| ____|
            | (___| |    | || | | | |___
            \___ \| |___ | || |_| | |___
            |____/|_|___|___|____/|_____|


            Modular Payload Generation Tool
                

                Develop a modular payload generation tool capable of producing evasion-ready payloads for:
                - Cross-Site Scripting (XSS)
                - SQL Injection (SQLi)
                - Command Injection (CMDi)

                Features:
                - Bypass input validation
                - Evade Web Application Firewalls (WAFs)
                - Circumvent blacklist filters
                - Encode the Generated Payloads
                - Easy integration and customization

            usage: slide.py [-h] [--xss {reflected,stored,dom,evasion,all}] [--sqli {error,union,blind,all}] [--cmdi {linux,windows,all}] [--encode {base64,url,hex,unicode}] [--obfuscate] [--output {cli,json,clipboard}] [--appendfile]

            Modular Payload Generator Tool for XSS, SQLi, and CMDi

            options:
            -h, --help            show this help message and exit
            --xss {reflected,stored,dom,evasion,all}
                                    Generate XSS Payloads
            --sqli {error,union,blind,all}
                                    Type of SQL injection payload to generate
            --cmdi {linux,windows,all}
            --encode {base64,url,hex,unicode}
            --obfuscate
            --output {cli,json,clipboard}
            --appendfile          Append payloads to 'output.txt'
                
     
     
     
     
     
How to use :
     
     
            Usage:  python3 slide.py <flags> <flags> <flags> .........

            Flags:

            --xss=<type>          Generate XSS payloads (Types = reflected, stored, dom, evasion, all)
            --sqli=<type>         Generate SQLi payloads (Types = error, union, blind, all)
            --cmdi=<type>         Generate CMDi payloads (Types = linux, windows, all)
            --appendfile           Append payloads to output files (xss_payload.txt, sqli_payload.txt, cmdi_payload.txt)
            --encode=<type>       Encode payloads (Types = base64, url, hex, unicode)
            --obfuscate           Obfuscate payloads to evade detection
            --output=<type>       Output format (Types = cli, json, clipboard) 
            --help                Show help message and exit


Example Usage is for CLI:
    python3 slide.py --xss=reflected --append --encode=base64 --obfuscate


For use in GUI
        pip install flask
        python3 run app.py


and that is all.