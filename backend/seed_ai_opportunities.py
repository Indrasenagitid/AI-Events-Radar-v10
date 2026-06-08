import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

opportunities = [

(
"World Summit AI Registration",
"Conference",
"World Summit AI",
"World Summit AI",
"Global",
"2026",
"Open",
100,
"https://worldsummit.ai",
"Active"
),

(
"NVIDIA GTC Registration",
"Conference",
"NVIDIA",
"NVIDIA",
"Global",
"2026",
"Open",
100,
"https://www.nvidia.com/gtc",
"Active"
),

(
"Microsoft Build Registration",
"Conference",
"Microsoft",
"Microsoft",
"Global",
"2026",
"Open",
100,
"https://build.microsoft.com",
"Active"
),

(
"India AI Impact Summit",
"Summit",
"IndiaAI",
"Government of India",
"India",
"2026",
"Open",
95,
"https://impact.indiaai.gov.in",
"Active"
),

(
"Cypher AI Conference",
"Conference",
"Analytics India Magazine",
"AIM",
"India",
"2026",
"Open",
90,
"https://cypher.analyticsindiamag.com",
"Active"
)

]

cursor.executemany("""
INSERT INTO ai_opportunities
(
title,
opportunity_type,
source,
organization,
region,
start_date,
deadline,
priority,
url,
status
)
VALUES (?,?,?,?,?,?,?,?,?,?)
""", opportunities)

conn.commit()

print("AI Opportunities seeded successfully")

conn.close()