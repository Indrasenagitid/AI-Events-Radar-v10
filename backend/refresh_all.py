import subprocess

print("Starting AI Events Radar refresh...\n")

print("Refreshing AI news...")
subprocess.run(["python", "ai_collector.py"])

print("\nRefreshing AI events...")
subprocess.run(["python", "ai_events_collector.py"])

print("\nRefresh completed successfully.")