@echo off
REM Navigate to the directory containing the docker-compose.yml file
cd /d C:\hasura

REM Run docker-compose up -d to start the containers
docker-compose down
docker-compose up -d

REM Pause the command prompt to see the output (optional)
pause
