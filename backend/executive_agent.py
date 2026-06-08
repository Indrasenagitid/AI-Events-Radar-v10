import sqlite3

def signal_text(count):
    return "signal" if count == 1 else "signals"
def get_executive_summary():

    conn = sqlite3.connect("data/events.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM ai_events")
    total_events = cursor.fetchone()[0]

    cursor.execute("""
        SELECT category, COUNT(*)
        FROM ai_events
        GROUP BY category
        ORDER BY COUNT(*) DESC
    """)
    categories = cursor.fetchall()

    cursor.execute("""
        SELECT technology, COUNT(*)
        FROM ai_events
        GROUP BY technology
        ORDER BY COUNT(*) DESC
    """)
    technologies = cursor.fetchall()

    cursor.execute("""
        SELECT source, COUNT(*)
        FROM ai_events
        GROUP BY source
        ORDER BY COUNT(*) DESC
    """)
    sources = cursor.fetchall()

    summary = "\nAI Events Radar Executive Summary\n"
    summary += f"\nTotal AI Events: {total_events}\n"

    summary += "\nCategory Breakdown:\n"
    for category, count in categories:
        summary += f"\n• {category}: {count}"

    summary += "\n\nTechnology Breakdown:\n"
    for technology, count in technologies:
        summary += f"\n• {technology}: {count}"

    summary += "\n\nSource Breakdown:\n"
    for source, count in sources:
        summary += f"\n• {source}: {count}"

    top_category = categories[0][0]
    top_category_count = categories[0][1]

    top_technology = technologies[0][0]
    top_technology_count = technologies[0][1]

    top_source = sources[0][0]
    top_source_count = sources[0][1]

    summary += "\n\nCEO Insight:\n"
    summary += f"The leading AI category is {top_category} with {top_category_count} {signal_text(top_category_count)}. "
    summary += f"The most active technology area is {top_technology} with {top_technology_count} {signal_text(top_technology_count)}. "
    summary += f"The most active source is {top_source} with {top_source_count} {signal_text(top_source_count)}. "
    summary += "This helps leadership understand where AI market activity is currently concentrated."

    summary += "\n\nExecutive Recommendation:\n"
    summary += f"Focus on {top_category} and continue monitoring major AI sources such as "
    summary += "Microsoft, Google, AWS, NVIDIA, and LangChain. "
    summary += f"{top_technology} should be tracked closely for future learning, hiring, and product strategy."

    conn.close()

    return summary


print(get_executive_summary())