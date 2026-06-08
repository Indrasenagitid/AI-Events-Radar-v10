import sqlite3
import os

DB_PATH = "data/events.db"

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_event_sources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    source_url TEXT NOT NULL UNIQUE,
    region TEXT NOT NULL,
    category TEXT NOT NULL,
    priority INTEGER NOT NULL,
    status TEXT NOT NULL
)
""")

sources = [
    ("World Summit AI", "https://worldsummit.ai", "Global", "AI Summit", 100, "Active"),
    ("NVIDIA GTC", "https://www.nvidia.com/gtc", "Global", "AI Infrastructure Summit", 100, "Active"),
    ("Microsoft Build", "https://build.microsoft.com", "Global", "AI Developer Conference", 100, "Active"),
    ("Data + AI Summit", "https://www.databricks.com/dataaisummit", "Global", "Data and AI Summit", 100, "Active"),
    ("Ai4 Conference", "https://ai4.io", "Global", "Enterprise AI Conference", 95, "Active"),
    ("AI for Good Global Summit", "https://aiforgood.itu.int", "Global", "AI Policy Summit", 95, "Active"),
    ("The AI Conference", "https://aiconference.com", "Global", "AI Engineering Conference", 90, "Active"),
    ("AI & Big Data Expo Global", "https://www.ai-expo.net/global", "Global", "Enterprise AI Expo", 90, "Active"),
    ("Reuters NEXT", "https://www.reuters.com/events", "Global", "Executive AI Event", 85, "Active"),
    ("Computex", "https://www.computextaipei.com.tw", "Global", "AI Hardware Event", 85, "Active"),

    ("India AI Impact Summit", "https://impact.indiaai.gov.in", "India", "Government AI Summit", 100, "Active"),
    ("Inc42 AI Summit", "https://events.inc42.com/ai-summit", "India", "Startup AI Summit", 95, "Active"),
    ("India AI Summit", "https://www.indiaaisummit.in", "India", "Enterprise AI Summit", 95, "Active"),
    ("NASSCOM AI Events", "https://nasscom.in", "India", "Enterprise AI Events", 90, "Active"),
    ("Data Science Congress India", "https://www.datasciencecongress.com", "India", "Data and AI Conference", 85, "Active"),
    ("Cypher AI Conference", "https://cypher.analyticsindiamag.com", "India", "AI Conference", 85, "Active"),
    ("AI Innovation Summit India", "https://www.aiinnovationsummit.in", "India", "Agentic AI Summit", 85, "Active"),
    ("IndiaAI Portal Events", "https://indiaai.gov.in", "India", "Government AI Events", 90, "Active"),
    ("T-Hub AI Events", "https://t-hub.co", "India", "Startup AI Events", 80, "Active"),
    ("Bengaluru Tech Summit", "https://bengalurutechsummit.com", "India", "Technology Summit", 80, "Active")
]

for source in sources:
    cursor.execute("""
    INSERT OR IGNORE INTO ai_event_sources
    (event_name, source_url, region, category, priority, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, source)

conn.commit()

cursor.execute("SELECT COUNT(*) FROM ai_event_sources")
count = cursor.fetchone()[0]

conn.close()

print(f"AI Event Sources table created successfully. Total sources: {count}")