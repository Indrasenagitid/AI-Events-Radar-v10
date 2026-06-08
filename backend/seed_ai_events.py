import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

events = [
    (
        "World Summit AI",
        "2026",
        "Amsterdam / Global",
        "https://worldsummit.ai",
        "World Summit AI",
        "Global",
        "AI Summit",
        100,
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ),
    (
        "NVIDIA GTC",
        "2026",
        "Global / Online",
        "https://www.nvidia.com/gtc",
        "NVIDIA GTC",
        "Global",
        "AI Infrastructure Summit",
        100,
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ),
    (
        "Microsoft Build",
        "2026",
        "Global / Online",
        "https://build.microsoft.com",
        "Microsoft Build",
        "Global",
        "AI Developer Conference",
        100,
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ),
    (
        "Data + AI Summit",
        "2026",
        "San Francisco / Online",
        "https://www.databricks.com/dataaisummit",
        "Databricks",
        "Global",
        "Data and AI Summit",
        100,
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ),
    (
        "India AI Impact Summit",
        "2026",
        "India",
        "https://impact.indiaai.gov.in",
        "IndiaAI",
        "India",
        "Government AI Summit",
        100,
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ),
    (
        "Inc42 AI Summit",
        "2026",
        "India / Online",
        "https://events.inc42.com/ai-summit",
        "Inc42",
        "India",
        "Startup AI Summit",
        95,
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
]

for event in events:
    cursor.execute("""
    INSERT OR IGNORE INTO ai_events
    (event_name, event_date, event_location, registration_url, source_name, region, category, priority, status, collected_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, event)

conn.commit()

cursor.execute("SELECT COUNT(*) FROM ai_events")
count = cursor.fetchone()[0]

conn.close()

print(f"AI Events seeded successfully. Total events: {count}")