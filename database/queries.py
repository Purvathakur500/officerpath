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
def add_study_session(user_id, subject, task_type, duration):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO StudySessions (user_id, subject, task_type, duration_minutes)
    VALUES (%s, %s, %s, %s);
    """

    cursor.execute(query, (user_id, subject, task_type, duration))
    connection.commit()

    cursor.close()
    connection.close()


def get_study_sessions():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject, task_type, duration_minutes, study_date
        FROM StudySessions
        ORDER BY study_date DESC;
    """)

    sessions = cursor.fetchall()

    cursor.close()
    connection.close()

    return sessions