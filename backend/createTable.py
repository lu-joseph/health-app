from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()


def createTable():
    conn = psycopg2.connect(host=os.getenv("DATABASE_HOST"),
                            database=os.getenv("DATABASE_NAME"),
                            user=os.getenv("DATABASE_USER"),
                            password=os.getenv("DATABASE_PASSWORD"))

    commands = (
        """
        CREATE TABLE mood (
            date DATE,
            score INTEGER
        )
        """,
        """
        CREATE TABLE exercise (
            date DATE,
            hours REAL
        )
        """,
        """
        CREATE TABLE sleep (
            date DATE,
            hours REAL
        )
        """,
        """
        CREATE TABLE food (
            date DATE,
            cals INTEGER
        )
        """,
        """
        CREATE TABLE water (
            date DATE,
            cups INTEGER
        )
        """,
        """
        CREATE TABLE screentime (
            date DATE,
            hours REAL
        )
        """
    )
    try:
        cur = conn.cursor()

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
