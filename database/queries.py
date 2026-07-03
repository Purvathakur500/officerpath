from database.db import get_connection
#----------
#adduser
#----------

def add_user(name, target_exam):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO Users (name, target_exam)
    VALUES (%s, %s)
    RETURNING user_id;
    """

    cursor.execute(query, (name, target_exam))

    user_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return user_id
#---
#get user 
#-------

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
#------------
#get study sessions
#-------------

def get_study_sessions(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject, task_type, duration_minutes, study_date
        FROM StudySessions
        WHERE user_id = %s
        ORDER BY study_date DESC;
    """, (user_id,))

    sessions = cursor.fetchall()

    cursor.close()
    connection.close()

    return sessions

#------------
#dashboard stats
#--------------
def get_dashboard_stats(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM StudySessions WHERE user_id = %s",
        (user_id,)
    )
    total_sessions = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COALESCE(SUM(duration_minutes),0)
        FROM StudySessions
        WHERE user_id = %s
        """,
        (user_id,)
    )
    total_minutes = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return total_sessions, total_minutes

def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, name, target_exam
        FROM Users
        ORDER BY name;
    """)

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users
