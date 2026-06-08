import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
SELECT event_name, region, category, priority, source_url
FROM ai_event_sources
ORDER BY priority DESC, region
""")

rows = cursor.fetchall()

print("\nAI Event Sources:\n")

for row in rows:
    print("Event:", row[0])
    print("Region:", row[1])
    print("Category:", row[2])
    print("Priority:", row[3])
    print("URL:", row[4])
    print("-" * 80)

conn.close()