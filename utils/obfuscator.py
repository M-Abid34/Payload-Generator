import re
import random

def obfuscate(payload):
    keywords = ['select', 'union', 'from', 'where', 'and', 'or', 'insert', 'update', 'delete', 'join', 'user', 'version']
    for kw in keywords:
        mixed = ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in kw)
        payload = re.sub(r'\b' + kw + r'\b', mixed, payload, flags=re.IGNORECASE)

    payload = re.sub(r'\s+', lambda m: f"/**/{' ' if random.random() > 0.5 else ''}", payload)

    payload = payload.replace("=1", "LIKE 1") if "1" in payload else payload

    return payload
