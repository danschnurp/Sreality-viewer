import json

import psycopg2
from flask import Flask, g, render_template
from psycopg2 import extras
from waitress import serve

app = Flask(__name__)
app.config.from_mapping(
)


# Define a function to create a database connection
def get_db():
    if 'db' not in g:
        # Connect to the database
        g.db = psycopg2.connect(
            host='db',
            port='5432',
            database='sreality',
            user='postgres',
            password='sreality'
        )
    return g.db


# Define a function to close the database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


# Define a function to query the database
def query_db(query, args=(), one=False):
    cur = get_db().cursor(cursor_factory=extras.DictCursor)
    cur.execute(query, args)
    results = cur.fetchall()
    cur.close()
    return (results[0] if results else None) if one else results


# Define a route to fetch data from the database
@app.route("/")
def get_data():
    results = query_db("SELECT url_part, title, img FROM results")
    # getting the pictures for simplicity
    for i in results:
        parted_pictues = i[2].split("\"")
        i[2] = [parted_pictues[1], parted_pictues[3], parted_pictues[5]]
    # viewing 10 results only due to politeness for seznam cz
    return render_template('index.html', results=results[50:60])



if __name__ == '__main__':
    print("db is scripted...")
    serve(app, port=8080)
    close_db()
