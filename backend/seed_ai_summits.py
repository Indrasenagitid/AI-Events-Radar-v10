import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

summits = [
    ("World Summit AI", "2026", "Amsterdam / Global", "https://worldsummit.ai", "World Summit AI", "Global", "AI Summit", 100, "Upcoming"),
    ("NVIDIA GTC", "2026", "Global / Online", "https://www.nvidia.com/gtc", "NVIDIA", "Global", "AI Infrastructure Summit", 100, "Upcoming"),
    ("Microsoft Build", "2026", "Global / Online", "https://build.microsoft.com", "Microsoft", "Global", "AI Developer Conference", 100, "Upcoming"),
    ("Data + AI Summit", "2026", "San Francisco / Online", "https://www.databricks.com/dataaisummit", "Databricks", "Global", "Data and AI Summit", 100, "Upcoming"),
    ("Ai4 Conference", "2026", "Las Vegas / Global", "https://ai4.io", "Ai4", "Global", "Enterprise AI Conference", 95, "Upcoming"),
    ("AI for Good Global Summit", "2026", "Geneva / Global", "https://aiforgood.itu.int", "ITU", "Global", "AI Policy Summit", 95, "Upcoming"),
    ("The AI Conference", "2026", "Global", "https://aiconference.com", "The AI Conference", "Global", "AI Engineering Conference", 90, "Upcoming"),
    ("AI & Big Data Expo Global", "2026", "Global", "https://www.ai-expo.net/global", "TechEx", "Global", "Enterprise AI Expo", 90, "Upcoming"),
    ("Reuters NEXT", "2026", "Global", "https://www.reuters.com/events", "Reuters", "Global", "Executive AI Event", 85, "Upcoming"),
    ("Computex", "2026", "Taipei", "https://www.computextaipei.com.tw", "Computex", "Global", "AI Hardware Event", 85, "Upcoming"),

    ("India AI Impact Summit", "2026", "India", "https://impact.indiaai.gov.in", "IndiaAI", "India", "Government AI Summit", 100, "Upcoming"),
    ("Inc42 AI Summit", "2026", "India / Online", "https://events.inc42.com/ai-summit", "Inc42", "India", "Startup AI Summit", 95, "Upcoming"),
    ("India AI Summit", "2026", "India", "https://www.indiaaisummit.in", "Elets", "India", "Enterprise AI Summit", 95, "Upcoming"),
    ("NASSCOM AI Events", "2026", "India", "https://nasscom.in", "NASSCOM", "India", "Enterprise AI Events", 90, "Upcoming"),
    ("Data Science Congress India", "2026", "India", "https://www.datasciencecongress.com", "DSCI", "India", "Data and AI Conference", 85, "Upcoming"),
    ("Cypher AI Conference", "2026", "India", "https://cypher.analyticsindiamag.com", "Analytics India Magazine", "India", "AI Conference", 85, "Upcoming"),
    ("AI Innovation Summit India", "2026", "India", "https://www.aiinnovationsummit.in", "AI Innovation Summit", "India", "Agentic AI Summit", 85, "Upcoming"),
    ("IndiaAI Portal Events", "2026", "India", "https://indiaai.gov.in", "IndiaAI", "India", "Government AI Events", 90, "Upcoming"),
    ("T-Hub AI Events", "2026", "Hyderabad, India", "https://t-hub.co", "T-Hub", "India", "Startup AI Events", 80, "Upcoming"),
    ("Bengaluru Tech Summit", "2026", "Bengaluru, India", "https://bengalurutechsummit.com", "Bengaluru Tech Summit", "India", "Technology Summit", 80, "Upcoming"),
]

for summit in summits:
    cursor.execute("""
    INSERT OR IGNORE INTO ai_summits
    (event_name, event_date, event_location, registration_url, source_name, region, category, priority, status, collected_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        summit[0],
        summit[1],
        summit[2],
        summit[3],
        summit[4],
        summit[5],
        summit[6],
        summit[7],
        summit[8],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

conn.commit()

cursor.execute("SELECT COUNT(*) FROM ai_summits")
count = cursor.fetchone()[0]

conn.close()

print(f"AI Summits seeded successfully. Total summits: {count}")