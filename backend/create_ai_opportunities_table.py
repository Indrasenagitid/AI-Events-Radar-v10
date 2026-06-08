import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,
    opportunity_type TEXT,

    source TEXT,
    organization TEXT,

    region TEXT,

    start_date TEXT,
    deadline TEXT,

    priority INTEGER,

    url TEXT,

    status TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("AI Opportunities table created successfully")

conn.close()