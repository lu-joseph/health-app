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
        "DROP TABLE exercise",
        "DROP TABLE sleep",
        "DROP TABLE food",
        "DROP TABLE water",
        "DROP TABLE screentime",
    )

    commands = (
        """
        CREATE TABLE mood (
            id SERIAL PRIMARY KEY,
            date DATE,
            score INTEGER
        )
        """,
        """
        CREATE TABLE exercise (
            id SERIAL PRIMARY KEY,
            date DATE,
            hours REAL
        )
        """,
        """
        CREATE TABLE sleep (
            id SERIAL PRIMARY KEY,
            date DATE,
            hours REAL
        )
        """,
        """
        CREATE TABLE food (
            id SERIAL PRIMARY KEY,
            date DATE,
            cals INTEGER
        )
        """,
        """
        CREATE TABLE water (
            id SERIAL PRIMARY KEY,
            date DATE,
            cups INTEGER
        )
        """,
        """
        CREATE TABLE screentime (
            id SERIAL PRIMARY KEY,
            date DATE,
            hours REAL
        )
        """
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
