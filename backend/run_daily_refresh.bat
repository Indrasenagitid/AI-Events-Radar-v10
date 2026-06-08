@echo off

cd /d C:\Users\ADMIN\AI-Events-Radar-v10\backend

call venv\Scripts\activate

python refresh_all.py

pause