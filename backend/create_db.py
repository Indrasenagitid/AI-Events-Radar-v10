import sqlite3
import os

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/events.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    source TEXT,
    technology TEXT,
    score INTEGER,
    status TEXT
)
""")

cursor.execute("DELETE FROM ai_events")

sample_data = [
    ("Microsoft AutoGen Release Notes","Release Notes","Microsoft","Agentic AI",100,"Live"),
    ("Google Gemini Release Notes","Release Notes","Google","Generative AI",100,"Live"),
    ("AWS Machine Learning Blog","News","AWS","Machine Learning",95,"Live"),
    ("NVIDIA AI Summit","Event","NVIDIA","AI Infrastructure",98,"Live"),
    ("LangGraph Learning Series","Learning","LangChain","LangGraph",92,"Live")
]

cursor.executemany("""
INSERT INTO ai_events
(title, category, source, technology, score, status)
VALUES (?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()

print("Database Created Successfully!")

conn.close()