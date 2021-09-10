import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
# Username is the email of user
create_table = "CREATE TABLE IF NOT EXISTS users (username text PRIMARY KEY, password text, price INTEGER)"
cursor.execute(create_table)



connection.commit()

connection.close()
