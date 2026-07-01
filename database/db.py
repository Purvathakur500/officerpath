import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="officerpath",
        user="postgres",
        password="Purva@24",
        port="5432"
    )