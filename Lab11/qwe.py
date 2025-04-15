
import psycopg2

def connect():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="usr1",
        password="3.14159",
        host="localhost",
        port="5432"
    )

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def insert_or_update(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_many(names, phones):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s, %s);", (names, phones))
    conn.commit()
    cur.close()
    conn.close()

def get_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_users(%s, %s);", (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def delete_user(identifier):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s);", (identifier,))
    conn.commit()
    cur.close()
    conn.close()


insert_or_update("Nartay", "+77015110211")