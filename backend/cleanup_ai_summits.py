import sqlite3

conn = sqlite3.connect("data/events.db")
cursor = conn.cursor()

# 1. Fix region spaces/case
cursor.execute("""
UPDATE ai_summits
SET region = TRIM(region)
""")

# 2. Move old / unclear / suspicious sources to Archive
archive_urls = [
    "https://www.datasciencecongress.com",
    "https://www.indiaaisummit.in"
]

for url in archive_urls:
    cursor.execute("""
    UPDATE ai_summits
    SET status = 'Archive'
    WHERE registration_url = ?
    """, (url,))

# 3. Keep only verified useful sources as Upcoming
verified_urls = [
    "https://worldsummit.ai",
    "https://www.nvidia.com/gtc",
    "https://build.microsoft.com",
    "https://www.databricks.com/dataaisummit",
    "https://ai4.io",
    "https://aiforgood.itu.int",
    "https://aiconference.com",
    "https://www.ai-expo.net/global",
    "https://www.reuters.com/events",
    "https://www.computextaipei.com.tw",
    "https://impact.indiaai.gov.in",
    "https://events.inc42.com/ai-summit",
    "https://nasscom.in",
    "https://indiaai.gov.in",
    "https://cypher.analyticsindiamag.com",
    "https://www.aiinnovationsummit.in",
    "https://t-hub.co",
    "https://bengalurutechsummit.com"
]

for url in verified_urls:
    cursor.execute("""
    UPDATE ai_summits
    SET status = 'Upcoming'
    WHERE registration_url = ?
    """, (url,))

conn.commit()

cursor.execute("""
SELECT event_name, region, status, registration_url
FROM ai_summits
ORDER BY status, region, priority DESC
""")

rows = cursor.fetchall()

print("\nAI Summits Cleanup Completed\n")

for row in rows:
    print(row)

conn.close()