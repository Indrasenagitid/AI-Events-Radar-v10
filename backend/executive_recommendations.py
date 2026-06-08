import sqlite3

DB_PATH = "data/events.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("\n🚀 EXECUTIVE AI RECOMMENDATIONS\n")

cursor.execute("""
SELECT event_name, region, priority
FROM ai_summits
WHERE status='Upcoming'
ORDER BY priority DESC
LIMIT 5
""")

events = cursor.fetchall()

for i, event in enumerate(events, start=1):
    print(f"{i}. {event[0]}")
    print(f"   Region: {event[1]}")
    print(f"   Priority: {event[2]}")
    print()

conn.close()