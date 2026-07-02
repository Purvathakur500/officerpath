from database.db import get_connection

connection = get_connection()
cursor = connection.cursor()

with open("database/schema.sql", "r") as file:
    sql = file.read()

cursor.execute(sql)

connection.commit()

print("✅ Tables created successfully!")

cursor.close()
connection.close()