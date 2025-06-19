import random

def obfuscate(payload):
    if "'" in payload or "select" in payload.lower():
        return payload.replace("SELECT", "SE/**/LECT").replace("UNION", "UN/**/ION")
    return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in payload)