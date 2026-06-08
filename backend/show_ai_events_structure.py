import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(ai_events)")

columns = cursor.fetchall()

print("\nAI_EVENTS TABLE STRUCTURE\n")

for column in columns:
    print(column)

conn.close()