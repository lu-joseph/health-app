from dotenv import load_dotenv
import os
import sys
import psycopg2

load_dotenv()


def createTable():
    conn = psycopg2.connect(host=os.getenv("DATABASE_HOST"),
                            database=os.getenv("DATABASE_NAME"),
                            user=os.getenv("DATABASE_USER"),
                            password=os.getenv("DATABASE_PASSWORD"))

    drop = (
        "DROP TABLE mood",
        "DROP TABLE activity",
        "DROP TABLE sleep",
        "DROP TABLE food",
        "DROP TABLE water",
        "DROP TABLE screentime",
        "DROP TABLE userdata"
    )

    commands = (
        """
        CREATE TABLE mood (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL UNIQUE,
            score INTEGER NOT NULL,
            userid INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE activity (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL UNIQUE,
            hours REAL NOT NULL,
            userid INTEGER NOT NULL
        ) er
        """,
        """
        CREATE TABLE sleep (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL UNIQUE,
            hours REAL NOT NULL,
            userid INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE food (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL UNIQUE,
            cals INTEGER NOT NULL,
            userid INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE water (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL UNIQUE,
            cups INTEGER NOT NULL,
            userid INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE screentime (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL UNIQUE,
            hours REAL NOT NULL,
            userid INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE userdata (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            sex VARCHAR(1) NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            age INTEGER NOT NULL
        )
        """  # sex must be 'M' or 'F'
    )
    try:
        cur = conn.cursor()
        print("arg is: " + sys.argv[1])
        if (len(sys.argv) == 2 and sys.argv[1] == "drop"):
            print("dropping old tables")
            for d in drop:
                cur.execute(d)
        conn.commit()

        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    createTable()
