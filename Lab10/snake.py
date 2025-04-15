import psycopg2

def connect():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="usr1",
        password="3.14159",
        host="localhost",
        port="5432"
    )

def save_score(username, score):
    conn = connect()
    cur = conn.cursor()

    # Проверяем, существует ли пользователь
    cur.execute("SELECT id FROM Users WHERE username = %s;", (username,))
    user = cur.fetchone()

    if not user:
        # Если пользователя нет, создаем нового
        cur.execute("INSERT INTO Users (username) VALUES (%s) RETURNING id;", (username,))
        user_id = cur.fetchone()[0]
        cur.execute("INSERT INTO UserScores (user_id, score) VALUES (%s, %s);", (user_id, score))
    else:
        user_id = user[0]
        # Если пользователь существует, проверяем, улучшился ли его рекорд
        cur.execute("SELECT score FROM UserScores WHERE user_id = %s;", (user_id,))
        current_score = cur.fetchone()[0]

        if score > current_score:
            cur.execute("UPDATE UserScores SET score = %s WHERE user_id = %s;", (score, user_id))

    conn.commit()
    cur.close()
    conn.close()