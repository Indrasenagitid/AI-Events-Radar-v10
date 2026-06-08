import sqlite3

DB_PATH = "data/events.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

opportunities = [
    (
        "Microsoft Azure AI Engineer Certification",
        "Certification",
        "Microsoft Learn",
        "Microsoft",
        "Global",
        "2026",
        "Open",
        95,
        "https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/",
        "Active"
    ),
    (
        "Google Cloud Generative AI Learning Path",
        "Certification",
        "Google Cloud Skills Boost",
        "Google",
        "Global",
        "2026",
        "Open",
        90,
        "https://www.cloudskillsboost.google/paths",
        "Active"
    ),
    (
        "AWS AI Practitioner Certification",
        "Certification",
        "AWS Skill Builder",
        "AWS",
        "Global",
        "2026",
        "Open",
        90,
        "https://skillbuilder.aws/",
        "Active"
    ),
    (
        "NVIDIA Deep Learning Institute Training",
        "Training",
        "NVIDIA DLI",
        "NVIDIA",
        "Global",
        "2026",
        "Open",
        90,
        "https://www.nvidia.com/en-us/training/",
        "Active"
    ),
    (
        "DeepLearning.AI Short Courses",
        "Training",
        "DeepLearning.AI",
        "DeepLearning.AI",
        "Global",
        "2026",
        "Open",
        85,
        "https://www.deeplearning.ai/short-courses/",
        "Active"
    ),
    (
        "Kaggle AI Competitions",
        "Hackathon",
        "Kaggle",
        "Google",
        "Global",
        "2026",
        "Open",
        85,
        "https://www.kaggle.com/competitions",
        "Active"
    ),
    (
        "Devpost AI Hackathons",
        "Hackathon",
        "Devpost",
        "Devpost",
        "Global",
        "2026",
        "Open",
        80,
        "https://devpost.com/hackathons",
        "Active"
    ),
    (
        "AWS AI and ML Webinars",
        "Webinar",
        "AWS Events",
        "AWS",
        "Global",
        "2026",
        "Open",
        80,
        "https://aws.amazon.com/events/",
        "Active"
    ),
    (
        "Microsoft AI Events and Webinars",
        "Webinar",
        "Microsoft Events",
        "Microsoft",
        "Global",
        "2026",
        "Open",
        80,
        "https://events.microsoft.com/",
        "Active"
    ),
    (
        "Google Cloud AI Events",
        "Webinar",
        "Google Cloud Events",
        "Google",
        "Global",
        "2026",
        "Open",
        80,
        "https://cloud.google.com/events",
        "Active"
    ),
    (
        "OpenAI Careers",
        "AI Jobs",
        "OpenAI Careers",
        "OpenAI",
        "Global",
        "2026",
        "Open",
        85,
        "https://openai.com/careers/",
        "Active"
    ),
    (
        "Anthropic Careers",
        "AI Jobs",
        "Anthropic Careers",
        "Anthropic",
        "Global",
        "2026",
        "Open",
        85,
        "https://www.anthropic.com/careers",
        "Active"
    ),
    (
        "NVIDIA AI Careers",
        "AI Jobs",
        "NVIDIA Careers",
        "NVIDIA",
        "Global",
        "2026",
        "Open",
        85,
        "https://www.nvidia.com/en-us/about-nvidia/careers/",
        "Active"
    ),
    (
        "IndiaAI Mission Updates",
        "Government AI Program",
        "IndiaAI",
        "Government of India",
        "India",
        "2026",
        "Open",
        90,
        "https://indiaai.gov.in/",
        "Active"
    ),
    (
        "Startup India AI Programs",
        "Startup Program",
        "Startup India",
        "Government of India",
        "India",
        "2026",
        "Open",
        80,
        "https://www.startupindia.gov.in/",
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
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", opportunities)

conn.commit()

cursor.execute("SELECT COUNT(*) FROM ai_opportunities")
count = cursor.fetchone()[0]

conn.close()

print(f"More AI opportunities seeded successfully. Total opportunities: {count}")