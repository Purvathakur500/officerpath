from database.db import get_connection


def add_user(name, target_exam):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Users (name, target_exam)
    VALUES (%s, %s);
    """

    cursor.execute(query, (name, target_exam))
    connection.commit()

    cursor.close()
    connection.close()


def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users")

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users