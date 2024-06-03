@echo off
:: Check Docker installation
docker --version
IF %ERRORLEVEL% NEQ 0 (
    echo Docker not installed. Installation of Docker...
    powershell -Command "Invoke-WebRequest -Uri https://get.docker.com/ -UseBasicParsing | Invoke-Expression"
)
net start com.docker.service

:: Check Grafana container
docker ps | findstr grafana
IF %ERRORLEVEL% NEQ 0 (
    echo Démarrage de Grafana...
    docker run -d -p 3000:3000 --name=grafana grafana/grafana
)

:: Python dependencies
pip install -r requirements.txt
python main.py

:: Open Grafana
start http://localhost:3000