import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_date TEXT,
    event_location TEXT,
    registration_url TEXT UNIQUE,
    source_name TEXT,
    region TEXT,
    category TEXT,
    priority INTEGER,
    status TEXT,
    collected_at TEXT
)
""")

conn.commit()
conn.close()

print("AI Events table created successfully")