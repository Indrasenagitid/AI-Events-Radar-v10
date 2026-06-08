import sqlite3
from datetime import datetime

DB_PATH = "data/events.db"

EVENT_SOURCES = [
    {
        "event_name": "World Summit AI",
        "event_date": "2026",
        "event_location": "Amsterdam / Global",
        "registration_url": "https://worldsummit.ai",
        "source_name": "World Summit AI",
        "region": "Global",
        "category": "AI Summit",
        "priority": 100
    },
    {
        "event_name": "NVIDIA GTC",
        "event_date": "2026",
        "event_location": "Global / Online",
        "registration_url": "https://www.nvidia.com/gtc",
        "source_name": "NVIDIA",
        "region": "Global",
        "category": "AI Infrastructure Summit",
        "priority": 100
    },
    {
        "event_name": "Microsoft Build",
        "event_date": "2026",
        "event_location": "Global / Online",
        "registration_url": "https://build.microsoft.com",
        "source_name": "Microsoft",
        "region": "Global",
        "category": "AI Developer Conference",
        "priority": 100
    },
    {
        "event_name": "Data + AI Summit",
        "event_date": "2026",
        "event_location": "San Francisco / Online",
        "registration_url": "https://www.databricks.com/dataaisummit",
        "source_name": "Databricks",
        "region": "Global",
        "category": "Data and AI Summit",
        "priority": 100
    },
    {
        "event_name": "India AI Impact Summit",
        "event_date": "2026",
        "event_location": "India",
        "registration_url": "https://impact.indiaai.gov.in",
        "source_name": "IndiaAI",
        "region": "India",
        "category": "Government AI Summit",
        "priority": 100
    },
    {
        "event_name": "Ai4 Conference",
        "event_date": "2026",
        "event_location": "Las Vegas / Global",
        "registration_url": "https://ai4.io",
        "source_name": "Ai4",
        "region": "Global",
        "category": "Enterprise AI Conference",
        "priority": 95
    },
    {
        "event_name": "AI for Good Global Summit",
        "event_date": "2026",
        "event_location": "Geneva / Global",
        "registration_url": "https://aiforgood.itu.int",
        "source_name": "ITU",
        "region": "Global",
        "category": "AI Policy Summit",
        "priority": 95
    },
    {
        "event_name": "Inc42 AI Summit",
        "event_date": "2026",
        "event_location": "India / Online",
        "registration_url": "https://events.inc42.com/ai-summit",
        "source_name": "Inc42",
        "region": "India",
        "category": "Startup AI Summit",
        "priority": 95
    },
    {
        "event_name": "Cypher AI Conference",
        "event_date": "2026",
        "event_location": "India",
        "registration_url": "https://cypher.analyticsindiamag.com",
        "source_name": "Analytics India Magazine",
        "region": "India",
        "category": "AI Conference",
        "priority": 85
    },
    {
        "event_name": "AI Innovation Summit India",
        "event_date": "2026",
        "event_location": "India",
        "registration_url": "https://www.aiinnovationsummit.in",
        "source_name": "AI Innovation Summit",
        "region": "India",
        "category": "Agentic AI Summit",
        "priority": 85
    },
    {
        "event_name": "T-Hub AI Events",
        "event_date": "2026",
        "event_location": "Hyderabad, India",
        "registration_url": "https://t-hub.co",
        "source_name": "T-Hub",
        "region": "India",
        "category": "Startup AI Events",
        "priority": 80
    },
    {
        "event_name": "Bengaluru Tech Summit",
        "event_date": "2026",
        "event_location": "Bengaluru, India",
        "registration_url": "https://bengalurutechsummit.com",
        "source_name": "Bengaluru Tech Summit",
        "region": "India",
        "category": "Technology Summit",
        "priority": 80
    }
]


def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ai_summits (
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


def upsert_event(event):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO ai_summits
    (
        event_name,
        event_date,
        event_location,
        registration_url,
        source_name,
        region,
        category,
        priority,
        status,
        collected_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        event["event_name"],
        event["event_date"],
        event["event_location"],
        event["registration_url"],
        event["source_name"],
        event["region"],
        event["category"],
        event["priority"],
        "Upcoming",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def collect_ai_events():
    create_table()

    added_or_updated = 0

    for event in EVENT_SOURCES:
        upsert_event(event)
        added_or_updated += 1

    print(f"AI Events Collector completed. Events added/updated: {added_or_updated}")


if __name__ == "__main__":
    collect_ai_events()