import bcrypt
import os

password = 'Magic123'

def hash_password(password):
    salt = bcrypt.gensalt()
    biany_password = password.encode('utf-8')
    hashed = bcrypt.hashpw(biany_password, salt)
    return hashed.decode('utf-8')
password = 'Magic123'
hashed_password = hash_password(password)
def verify_password(password, hashed):
    biany_password = password.encode('utf-8')
    return bcrypt.checkpw(biany_password, hashed.encode('utf-8'))
is_valid = verify_password('Magic123', hashed_password)
print(f"Hashed Password: {hashed_password}")
print(f"Password is valid: {is_valid}")

def register_user(username, password):
    hashed = hash_password(password)
    # Check if username already exists
    try:
        with open('user.text', 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ',' not in line:
                    continue  # Skip empty or malformed lines
                stored_username, stored_hashed = line.split(',', 1)
                if username == stored_username:
                    print("Username already exists.")
                    return False
    except FileNotFoundError:
        pass  # File doesn't exist yet, will be created
    # Store new user
    with open('user.text', 'a') as f:
        f.write(f"{username},{hashed}\n")
    return True

def login_in(username, password):
    try:
        with open('user.text', 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ',' not in line:
                    continue  # Skip empty or malformed lines
                stored_username, stored_hashed = line.split(',', 1)
                if username == stored_username:
                    return verify_password(password, stored_hashed)
    except FileNotFoundError:
        return False
    return False
def menu ():
    while True:
        print("\n1) Register")
        print("2) Login")
        print("3) Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if register_user(username, password):
                print("Registration successful.")            
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_in(username, password):
                print("Login successful.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            print("Goodbye!")
            break

import sqlite3

DB_PATH = 'DATA/telligence_platform.db'

def init_db():
    # Ensure directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    sql = ("""CREATE TABLE IF NOT EXISTS USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    );""")
    curr.execute(sql)
    conn.commit()
    conn.close()
