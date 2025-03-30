import psycopg2
import csv

def connect():
    return psycopg2.connect(
        #думал сделать хост что бы любой мог посмотреть по этим данным но смысла нету
        dbname="phonebook_db",
        user="usr1",
        password="3.14159",
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS UserScores (
            id SERIAL PRIMARY KEY,
            user_id INT REFERENCES Users(id),
            score INT DEFAULT 0,
            level INT DEFAULT 1
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()

def update_phonebook(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s;", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()

def query_phonebook():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_from_phonebook(identifier):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s;", (identifier, identifier))
    conn.commit()
    cur.close()
    conn.close()

def snake_game():
    username = input("Enter your username: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM Users WHERE username = %s;", (username,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO Users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO UserScores (user_id) VALUES (%s);", (user_id,))
    else:
        user_id = user[0]
    
    cur.execute("SELECT score, level FROM UserScores WHERE user_id = %s;", (user_id,))
    score, level = cur.fetchone()
    print(f"Welcome {username}, your current level: {level}, score: {score}")
    
    conn.commit()
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    create_tables()
