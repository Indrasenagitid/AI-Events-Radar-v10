from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "data/events.db"


@app.get("/")
def home():
    return {
        "message": "AI Events Radar Backend is running"
    }


def parse_published_date(date_text):
    try:
        return parsedate_to_datetime(date_text)
    except Exception:
        return None


@app.get("/ai-updates")
def get_ai_updates():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, source, technology, published, link
        FROM ai_updates
    """)

    rows = cursor.fetchall()
    conn.close()

    now = datetime.now(timezone.utc)
    cutoff_date = now - timedelta(days=30)

    updates = []

    for row in rows:
        published_date = parse_published_date(row[3])

        if published_date is None:
            continue

        if published_date.tzinfo is None:
            published_date = published_date.replace(tzinfo=timezone.utc)

        if published_date >= cutoff_date:
            updates.append({
                "title": row[0],
                "source": row[1],
                "technology": row[2],
                "published": row[3],
                "link": row[4],
                "published_sort": published_date
            })

    updates.sort(key=lambda x: x["published_sort"], reverse=True)

    final_updates = []

    for update in updates[:20]:
        final_updates.append({
            "title": update["title"],
            "source": update["source"],
            "technology": update["technology"],
            "published": update["published"],
            "link": update["link"]
        })

    return {
        "total": len(final_updates),
        "updates": final_updates
    }


@app.get("/ai-summits")
def get_ai_summits():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT event_name, event_date, event_location, registration_url,
               source_name, region, category, priority, status
        FROM ai_summits
        WHERE TRIM(status) = 'Upcoming'
        ORDER BY priority DESC, region
    """)

    rows = cursor.fetchall()
    conn.close()

    summits = []

    for row in rows:
        summits.append({
            "event_name": row[0],
            "event_date": row[1],
            "event_location": row[2],
            "registration_url": row[3],
            "source_name": row[4],
            "region": row[5],
            "category": row[6],
            "priority": row[7],
            "status": row[8]
        })

    return {
        "total": len(summits),
        "summits": summits
    }


@app.get("/ai-opportunities")
def get_ai_opportunities():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, opportunity_type, source, organization, region,
               start_date, deadline, priority, url, status
        FROM ai_opportunities
        WHERE TRIM(status) = 'Active'
        ORDER BY priority DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    opportunities = []

    for row in rows:
        opportunities.append({
            "title": row[0],
            "opportunity_type": row[1],
            "source": row[2],
            "organization": row[3],
            "region": row[4],
            "start_date": row[5],
            "deadline": row[6],
            "priority": row[7],
            "url": row[8],
            "status": row[9]
        })

    return {
        "total": len(opportunities),
        "opportunities": opportunities
    }