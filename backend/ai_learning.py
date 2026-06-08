import sqlite3

DB_PATH = "data/events.db"

learning_resources = [
    ("DeepLearning.AI", "https://www.deeplearning.ai", "Generative AI"),
    ("Microsoft Learn AI", "https://learn.microsoft.com", "Azure AI"),
    ("AWS Skill Builder", "https://skillbuilder.aws", "AWS AI"),
    ("Google Cloud Skills Boost", "https://www.cloudskillsboost.google", "Google AI"),
    ("Hugging Face Course", "https://huggingface.co/learn", "Open Source AI"),
    ("LangChain Academy", "https://academy.langchain.com", "Agentic AI"),
    ("Databricks Academy", "https://academy.databricks.com", "Data + AI"),
    ("NVIDIA DLI", "https://www.nvidia.com/training", "AI Infrastructure")
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_learning (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_name TEXT,
    url TEXT,
    category TEXT
)
""")

cursor.execute("DELETE FROM ai_learning")

cursor.executemany("""
INSERT INTO ai_learning (
    resource_name,
    url,
    category
)
VALUES (?, ?, ?)
""", learning_resources)

conn.commit()
conn.close()

print("AI Learning Resources Loaded Successfully")