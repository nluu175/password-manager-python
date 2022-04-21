import psycopg2
from config import config


# This function creates the table
def table_initializer(cur):
    # Create Table
    cur.execute(open("./queries/create_users_table.sql", "r").read())
    cur.execute(open("./queries/create_accounts_table.sql", "r").read())


def create_tables():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('|  Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute queries
        table_initializer(cur)
        print("|  Tables created!")

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("|  ", error)
    finally:
        if conn is not None:
            conn.close()
            print('|  Database connection closed.')


def create_user(username, password):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute queries
        cur.execute(f"INSERT INTO users(Username, Password) \
                     VALUES('{username}', '{password}');")

        print("| -- New account sucessfully created! ")

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("|  ", error)
    finally:
        if conn is not None:
            conn.close()
