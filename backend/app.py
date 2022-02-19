from sqlite3 import DatabaseError
from flask import Flask
from dotenv import load_dotenv
import psycopg2
import os
app = Flask(__name__)

load_dotenv()


@app.route("/")
def hello():
    conn = psycopg2.connect(host=os.getenv("DATABASE_HOST"),
                            database=os.getenv("DATABASE_NAME"),
                            user=os.getenv("DATABASE_USER"),
                            password=os.getenv("DATABASE_PASSWORD"))
    try:
        cur = conn.cursor()
        command = """
        CREATE TABLE test (
            id SERIAL PRIMARY KEY,
            colour VARCHAR(255) NOT NULL
        )
        """
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return "Hello World!"


if __name__ == "__main__":
    app.run()
