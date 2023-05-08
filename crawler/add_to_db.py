import psycopg2
import json


# simple script that inserts data from results.json to postgres DB

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="sreality",
        user="postgres",
        password="Praha123"
    )
    return conn


def insert_one_record(data):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO results (url_part, title, img)
        VALUES (%s, %s, %s)
    """, (data['url_part'], data['title'], data['img']))
    conn.commit()
    cur.close()
    conn.close()


def insert_cached_data(data):
    conn = connect_to_db()
    cur = conn.cursor()
    for i in data:
        cur.execute("""
            INSERT INTO results (url_part, title, img)
            VALUES (%s, %s, %s)
        """, (i['url_part'], i['title'], i['img']))

    conn.commit()
    cur.close()
    conn.close()


with open("../results.json") as f:
    results = json.loads(f.read())
insert_cached_data(results)
