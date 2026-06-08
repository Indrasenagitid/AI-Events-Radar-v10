import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM ai_summits
WHERE status = 'Archive'
""")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM ai_summits")
total = cursor.fetchone()[0]

conn.close()

print(f"Archive summits removed. Remaining summits: {total}")