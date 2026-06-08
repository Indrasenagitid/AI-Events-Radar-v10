import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime
import subprocess

DB_PATH = "backend/data/events.db"

st.set_page_config(
    page_title="AI Events Radar",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #f6f8fb;
}

.block-container {
    padding-top: 1rem;
    padding-left: 1.4rem;
    padding-right: 1.4rem;
}

.hero-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%);
    padding: 22px;
    border-radius: 20px;
    color: white;
    margin-bottom: 16px;
    box-shadow: 0 10px 28px rgba(15, 23, 42, 0.18);
}

.hero-title {
    font-size: 32px;
    font-weight: 900;
    margin-bottom: 4px;
}

.hero-subtitle {
    font-size: 14px;
    color: #dbeafe;
    max-width: 1100px;
}

.section-title {
    font-size: 21px;
    font-weight: 900;
    color: #111827;
    margin-top: 14px;
    margin-bottom: 10px;
}

.item-card {
    background: white;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    padding: 13px 15px;
    margin-bottom: 8px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
    transition: all 0.25s ease;
}

.item-card:hover {
    transform: translateY(-3px);
    border: 1px solid #2563eb;
    box-shadow: 0 14px 32px rgba(37, 99, 235, 0.18);
    background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
}

.item-card:hover .item-title {
    color: #1d4ed8;
}

.item-title {
    font-size: 16px;
    font-weight: 900;
    color: #111827;
    margin-bottom: 5px;
}

.item-text {
    font-size: 13px;
    color: #374151;
    margin-bottom: 2px;
}

.url-text {
    font-size: 11px;
    color: #64748b;
    word-break: break-all;
    margin-top: 5px;
}

.badge-high {
    display: inline-block;
    background: #fee2e2;
    color: #991b1b;
    padding: 4px 9px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 6px;
}

.badge-medium {
    display: inline-block;
    background: #fef3c7;
    color: #92400e;
    padding: 4px 9px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 6px;
}

.badge-blue {
    display: inline-block;
    background: #dbeafe;
    color: #1d4ed8;
    padding: 4px 9px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 6px;
}

.badge-green {
    display: inline-block;
    background: #dcfce7;
    color: #166534;
    padding: 4px 9px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 800;
    margin-bottom: 6px;
}

.stButton > button {
    transition: all 0.25s ease;
    border-radius: 12px;
    padding: 0.35rem 0.75rem;
    font-size: 13px;
}

.stButton > button:hover {
    background: #2563eb;
    color: white;
    border-color: #2563eb;
    transform: translateY(-2px);
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 12px 14px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

div[data-testid="stMetric"]:hover {
    border: 1px solid #2563eb;
    box-shadow: 0 12px 28px rgba(37, 99, 235, 0.12);
}

a {
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


def load_data(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def refresh_data():
    subprocess.run(
        ["python", "backend/refresh_all.py"],
        capture_output=True,
        text=True
    )


def event_card(row, badge_class="badge-blue", show_url=True):
    st.markdown(f"""
    <div class="item-card">
        <div class="{badge_class}">{row['region']} | Priority {row['priority']}</div>
        <div class="item-title">{row['event_name']}</div>
        <div class="item-text"><b>Category:</b> {row['category']}</div>
        <div class="item-text"><b>Location:</b> {row['event_location']}</div>
        <div class="item-text"><b>Source:</b> {row['source_name']}</div>
        {"<div class='url-text'>" + row["registration_url"] + "</div>" if show_url else ""}
    </div>
    """, unsafe_allow_html=True)

    st.link_button("🔗 Open Official Event Page", row["registration_url"])


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

learning_df = load_data("""
    SELECT resource_name, url, category
    FROM ai_learning
    ORDER BY category
""")

action_df = load_data("""
    SELECT priority, action_item, category
    FROM ai_action_center
    ORDER BY id
""")

updates_df = load_data("""
    SELECT title, source, technology, published, link
    FROM ai_updates
    ORDER BY id DESC
    LIMIT 5
""")

st.markdown("""
<div class="hero-card">
    <div class="hero-title">🚀 AI Events Radar</div>
    <div class="hero-subtitle">
        A live AI Opportunity Intelligence dashboard for tracking AI events, certifications,
        learning resources, technology updates, and executive actions in one place.
    </div>
</div>
""", unsafe_allow_html=True)

top_bar_left, top_bar_right = st.columns([1, 8])

with top_bar_left:
    if st.button("🔄 Refresh"):
        refresh_data()
        st.success("Updated")

with top_bar_right:
    st.info(f"Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.metric("Top Events", len(summits_df.head(5)))
with m2:
    st.metric("India Events", len(summits_df[summits_df["region"] == "India"].head(5)))
with m3:
    st.metric("Certifications", len(certifications_df))
with m4:
    st.metric("Learning", len(learning_df))
with m5:
    st.metric("AI Updates", len(updates_df))

st.markdown('<div class="section-title">🚨 Executive AI Action Center</div>', unsafe_allow_html=True)

action_cols = st.columns(3)

for index, row in action_df.iterrows():
    badge_class = "badge-high" if row["priority"] == "HIGH" else "badge-medium"

    with action_cols[index % 3]:
        st.markdown(f"""
        <div class="item-card">
            <div class="{badge_class}">{row['priority']} | {row['category']}</div>
            <div class="item-text">{row['action_item']}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🔥 Top AI Event Links for Testing</div>', unsafe_allow_html=True)

event_test_cols = st.columns(5)

for index, row in summits_df.head(5).iterrows():
    with event_test_cols[index % 5]:
        st.markdown(f"""
        <div class="item-card">
            <div class="badge-blue">Priority {row['priority']}</div>
            <div class="item-title">{row['event_name']}</div>
            <div class="item-text">{row['event_location']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Open", row["registration_url"])

left_col, right_col = st.columns(2)

with left_col:
    st.markdown('<div class="section-title">🔥 Executive AI Recommendations</div>', unsafe_allow_html=True)

    for _, row in summits_df.head(5).iterrows():
        event_card(row, "badge-blue", True)

    st.markdown('<div class="section-title">🇮🇳 India AI Events</div>', unsafe_allow_html=True)

    india_events = summits_df[summits_df["region"] == "India"].head(5)

    for _, row in india_events.iterrows():
        event_card(row, "badge-green", True)

with right_col:
    st.markdown('<div class="section-title">🎓 Recommended AI Certifications</div>', unsafe_allow_html=True)

    for _, row in certifications_df.head(8).iterrows():
        st.markdown(f"""
        <div class="item-card">
            <div class="badge-blue">{row['provider']} | {row['level']}</div>
            <div class="item-title">{row['certification_name']}</div>
            <div class="item-text"><b>Provider:</b> {row['provider']}</div>
            <div class="item-text"><b>Level:</b> {row['level']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">📚 AI Learning Hub</div>', unsafe_allow_html=True)

    for _, row in learning_df.head(6).iterrows():
        st.markdown(f"""
        <div class="item-card">
            <div class="badge-green">{row['category']}</div>
            <div class="item-title">{row['resource_name']}</div>
            <div class="item-text">Recommended learning source for {row['category']}.</div>
            <div class="url-text">{row['url']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("🔗 Open Learning Resource", row["url"])

    st.markdown('<div class="section-title">📰 Latest Important AI Updates</div>', unsafe_allow_html=True)

    for _, row in updates_df.iterrows():
        st.markdown(f"""
        <div class="item-card">
            <div class="badge-blue">{row['source']}</div>
            <div class="item-title">{row['title']}</div>
            <div class="item-text"><b>Technology:</b> {row['technology']}</div>
            <div class="url-text">{row['link']}</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("🔗 Open Update", row["link"])