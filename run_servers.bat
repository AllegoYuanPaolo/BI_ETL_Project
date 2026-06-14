@echo off

start "Backend Server" python "app/main.py"
start "Frontend Server" python "frontend/run.py"