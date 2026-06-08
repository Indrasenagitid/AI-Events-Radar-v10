import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
SELECT source, COUNT(*)
FROM ai_updates
GROUP BY source
""")

rows = cursor.fetchall()

print("\nUpdates By Source\n")

for row in rows:
    print(row[0], "=", row[1])

conn.close()