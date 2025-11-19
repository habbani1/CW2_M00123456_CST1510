import sqlite3


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


def add_user(conn, name, pwd_hash):
    curr = conn.cursor()
    sql = ("""INSERT INTO users (username, password_hash) VALUES (?, ?)""")
    params = (name, pwd_hash)
    curr.execute(sql, params)
    conn.commit()


if __name__ == "__main__":
    # ensure the table exists and import test user and print current users
    create_user_table("DATA/telligence_platform.db")
    with sqlite3.connect("DATA/telligence_platform.db") as conn:
        # attempt to add a test user (ignore if it already exists)
        try:
            add_user(conn, "testuser", "Habbani")
        except sqlite3.IntegrityError:
            pass

        curr = conn.cursor()
        curr.execute("SELECT * FROM users")
        users = curr.fetchall()
        print(users)

def get_all_users(conn):
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    users = curr.fetchall()
    return users

# Import users from a text file and add them to the database.
# The file is expected to have one user per line in the format: username,password_hash
def import_users_from_file(file_path="DATA/user.text", db_path="DATA/telligence_platform.db"):
    with open(file_path, "r") as f, sqlite3.connect(db_path) as conn:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                name, pwd_hash = parts[0].strip(), parts[1].strip()
                try:
                    add_user(conn, name, pwd_hash)
                except sqlite3.IntegrityError:
                    # ignore duplicates
                    pass

def get_all_users_pandas(db_path="DATA/telligence_platform.db"):
    import pandas as pd
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM users", conn)
    conn.close()
    return df

def main():
    create_user_table()
    import_users_from_file()
    df = get_all_users_pandas()
    print(df)
    def migrate():
        create_user_table()
        import_users_from_file()
        df = get_all_users_pandas()
        print(df)

if __name__ == "__main__":
    main()
    migrante