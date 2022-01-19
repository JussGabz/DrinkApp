import psycopg2
from config import config


def create_user_table():
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            surname VARCHAR(255),
            email VARCHAR(255),
            username VARCHAR(255),
            password VARCHAR(255)
        )"""
    )

    conn = None

    try:
        # Read connection parameters
        params = config()

        # Connect to Postgres
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Create Table
        cur.execute(commands)

        # close communication with the postgreSQL database server
        cur.close()

        # commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


create_user_table()
