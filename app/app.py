import psycopg2
from flask import Flask, g, render_template
from psycopg2 import extras
from waitress import serve

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE_HOST='localhost',
    DATABASE_PORT=5432,
    DATABASE_NAME='sreality',
    DATABASE_USER='postgres',
    DATABASE_PASSWORD="Praha123"
)


# Define a function to create a database connection
def get_db():
    if 'db' not in g:
        # Connect to the database
        g.db = psycopg2.connect(
            host=app.config['DATABASE_HOST'],
            port=app.config['DATABASE_PORT'],
            database=app.config['DATABASE_NAME'],
            user=app.config['DATABASE_USER'],
            password=app.config['DATABASE_PASSWORD']
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
    results = query_db("SELECT * FROM results")
    # getting the pictures for simplicity
    for i in results:
        parted_pictues = i[2].split("\"")
        i[2] = [parted_pictues[1], parted_pictues[3], parted_pictues[5]]

    return render_template('index.html', results=results[50:60])


if __name__ == '__main__':
    serve(app, port=8080)
    close_db()
