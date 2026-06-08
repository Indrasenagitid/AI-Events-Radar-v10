import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM ai_summits
WHERE status='Upcoming'
""")

upcoming = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM ai_summits
WHERE status='Archive'
""")

archive = cursor.fetchone()[0]

print("\nAI SUMMITS STATUS\n")
print("Upcoming:", upcoming)
print("Archive :", archive)

conn.close()