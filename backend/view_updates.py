import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
SELECT title, source, technology, published
FROM ai_updates
ORDER BY id DESC
LIMIT 10
""")

rows = cursor.fetchall()

print("\nLatest AI Updates:\n")

for row in rows:
    print("Title:", row[0])
    print("Source:", row[1])
    print("Technology:", row[2])
    print("Published:", row[3])
    print("-" * 80)

conn.close()