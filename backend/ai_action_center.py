import sqlite3

DB_PATH = "data/events.db"

actions = [
    ("HIGH", "Review and track top AI events for possible team participation", "Events"),
    ("HIGH", "Review latest AI updates from OpenAI, AWS, Google, Microsoft and NVIDIA", "News"),
    ("MEDIUM", "Identify AI certifications useful for internal team learning", "Certifications"),
    ("MEDIUM", "Review AI learning platforms for team skill development", "Learning"),
    ("MEDIUM", "Track India-focused AI events for local participation and networking", "India Events")
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_action_center (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    priority TEXT,
    action_item TEXT,
    category TEXT
)
""")

cursor.execute("DELETE FROM ai_action_center")

cursor.executemany("""
INSERT INTO ai_action_center (
    priority,
    action_item,
    category
)
VALUES (?, ?, ?)
""", actions)

conn.commit()
conn.close()

print("AI Action Center Loaded Successfully")