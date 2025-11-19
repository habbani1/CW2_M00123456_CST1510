def create_user_table(db_path="DATA/telligence_platform.db"):
    conn = sqlite3.connect(db_path)
    try:
        curr = conn.cursor()
        sql = ("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )""")
        curr.execute(sql)
        conn.commit()
    finally:
        conn.close()