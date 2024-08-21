@echo off

REM Run docker-compose up -d to start the containers
uvicorn main:app --reload

REM Pause the command prompt to see the output (optional)
pause
