import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime
import subprocess

DB_PATH = "data/events.db"

st.set_page_config(
    page_title="AI Events Radar",
    page_icon="🚀",
    layout="wide"
)


def load_data(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def refresh_data():
    subprocess.run(
        ["python", "refresh_all.py"],
        capture_output=True,
        text=True
    )


summits_df = load_data("""
    SELECT event_name, event_date, event_location, registration_url,
           source_name, region, category, priority, status
    FROM ai_summits
    WHERE status = 'Upcoming'
    ORDER BY priority DESC
""")

certifications_df = load_data("""
    SELECT certification_name, provider, level
    FROM ai_certifications
    ORDER BY provider
""")

updates_df = load_data("""
    SELECT title, source, technology, published, link
    FROM ai_updates
    ORDER BY id DESC
    LIMIT 5
""")

st.title("🚀 AI Events Radar")
st.caption("Simple AI opportunities dashboard for team and management action.")

col_a, col_b = st.columns([1, 5])

with col_a:
    if st.button("🔄 Refresh"):
        refresh_data()
        st.success("Updated")

with col_b:
    st.info(f"Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Top Events", len(summits_df.head(5)))
col2.metric("India Events", len(summits_df[summits_df["region"] == "India"].head(5)))
col3.metric("AI Certifications", len(certifications_df))
col4.metric("Latest Updates", len(updates_df))

st.divider()

left_col, right_col = st.columns(2)

with left_col:
    st.header("🔥 Executive AI Recommendations")

    for _, row in summits_df.head(5).iterrows():
        with st.container(border=True):
            st.subheader(row["event_name"])
            st.write(f"**Why:** High-priority {row['category']} for {row['region']}.")
            st.write(f"**Location:** {row['event_location']}")
            st.write(f"**Priority:** {row['priority']}")
            st.link_button("Open Event Page", row["registration_url"])

    st.header("🇮🇳 India AI Events")

    india_events = summits_df[summits_df["region"] == "India"].head(5)

    for _, row in india_events.iterrows():
        with st.container(border=True):
            st.subheader(row["event_name"])
            st.write(f"**Category:** {row['category']}")
            st.write(f"**Location:** {row['event_location']}")
            st.write(f"**Priority:** {row['priority']}")
            st.link_button("Open Event Page", row["registration_url"])


with right_col:
    st.header("🎓 Recommended AI Certifications")

    for _, row in certifications_df.head(10).iterrows():
        with st.container(border=True):
            st.subheader(row["certification_name"])
            st.write(f"**Provider:** {row['provider']}")
            st.write(f"**Level:** {row['level']}")

    st.header("📰 Latest Important AI Updates")

    for _, row in updates_df.iterrows():
        with st.container(border=True):
            st.subheader(row["title"])
            st.write(f"**Source:** {row['source']}")
            st.write(f"**Technology:** {row['technology']}")
            st.link_button("Open Update", row["link"])