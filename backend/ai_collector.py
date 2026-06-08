import sqlite3
import feedparser
from datetime import datetime

DB_PATH = "data/events.db"

AI_FEEDS = [
    {
        "source": "OpenAI Blog",
        "url": "https://openai.com/news/rss.xml",
        "category": "AI News",
        "technology": "OpenAI"
    },
    {
        "source": "Google AI Blog",
        "url": "https://blog.google/technology/ai/rss/",
        "category": "AI News",
        "technology": "Google AI"
    },
    {
        "source": "AWS Machine Learning Blog",
        "url": "https://aws.amazon.com/blogs/machine-learning/feed/",
        "category": "AI News",
        "technology": "AWS AI"
    },
    {
        "source": "NVIDIA AI Blog",
        "url": "https://blogs.nvidia.com/blog/category/deep-learning/feed/",
        "category": "AI News",
        "technology": "NVIDIA AI"
    },
    {
        "source": "Hugging Face Blog",
        "url": "https://huggingface.co/blog/feed.xml",
        "category": "AI News",
        "technology": "Open Source AI"
    },
    {
        "source": "LangChain Blog",
        "url": "https://blog.langchain.com/rss/",
        "category": "Agentic AI",
        "technology": "LangChain"
    },
    {
        "source": "Google Cloud AI Blog",
        "url": "https://cloud.google.com/blog/products/ai-machine-learning/rss",
        "category": "Cloud AI",
        "technology": "Google Cloud AI"
    },
    {
        "source": "Microsoft Azure AI Blog",
        "url": "https://techcommunity.microsoft.com/t5/azure-ai-services-blog/bg-p/AzureAIServicesBlog/rss",
        "category": "Cloud AI",
        "technology": "Microsoft Azure AI"
    },
    {
        "source": "Meta AI Blog",
        "url": "https://ai.meta.com/blog/rss/",
        "category": "AI Research",
        "technology": "Meta AI"
    },
    {
        "source": "Mistral AI News",
        "url": "https://mistral.ai/news/rss.xml",
        "category": "AI News",
        "technology": "Mistral AI"
    }
]

def create_ai_updates_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ai_updates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        link TEXT UNIQUE,
        source TEXT,
        category TEXT,
        technology TEXT,
        published TEXT,
        collected_at TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_update(title, link, source, category, technology, published):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO ai_updates
        (title, link, source, category, technology, published, collected_at, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            title,
            link,
            source,
            category,
            technology,
            published,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "New"
        ))
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

def collect_ai_updates():
    create_ai_updates_table()

    total_new = 0

    for feed in AI_FEEDS:
        print(f"Collecting from: {feed['source']}")

        parsed_feed = feedparser.parse(feed["url"])

        for entry in parsed_feed.entries[:10]:
            title = entry.get("title", "No Title")
            link = entry.get("link", "")
            published = entry.get("published", "Unknown")

            if not link:
                continue

            inserted = save_update(
                title=title,
                link=link,
                source=feed["source"],
                category=feed["category"],
                technology=feed["technology"],
                published=published
            )

            if inserted:
                total_new += 1

    print(f"AI Updates Collection Completed. New updates added: {total_new}")

if __name__ == "__main__":
    collect_ai_updates()