import psycopg2
from config import config


def connect():
    conn = None

    try:

        # read connection params
        params = config()

        print("connecting to database..")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print("Postgres Version:")
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database Connection closed.")


if __name__ == '__main__':
    connect()
