@echo off
title MiniCyc
color E
echo [MiniCyc] Starting MiniCyc...

:: Check Docker
echo [STEP 1/6] Checking Docker installation...
docker --version
IF %ERRORLEVEL% NEQ 0 (
    echo Docker not installed. Installation of Docker...
    powershell -Command "Invoke-WebRequest -Uri https://get.docker.com/ -UseBasicParsing | Invoke-Expression"
)

echo [STEP 2/6] Checking Docker service status...
sc query docker >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Docker service is not running. Starting Docker service...
    docker info >nul 2>&1
    if %errorlevel% neq 0 (
        echo Starting Docker...
        start "Docker" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
        timeout /t 10 /nobreak >nul
    )
) ELSE (
    echo Docker service is already running.
)

echo [STEP 3/6] Launching containers...
docker --version
docker-compose --version
cd grafanaStreaming
docker-compose up -d
cd ..

:: Check Python
echo [STEP 4/6] Installing Python...
IF NOT EXIST "%LocalAppData%\Programs\Python\Python312\python.exe" (
    echo Installing Python 3.12.3 64-bit...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -OutFile python-3.12.3-amd64.exe"
    python-3.12.3-amd64.exe /quiet InstallAllUsers=0 PrependPath=1
    del python-3.12.3-amd64.exe
) ELSE (
    echo Python 3.12.3 64-bits already installed
)
python --version

echo [STEP 5/6] Installing Python dependencies...
pip install -r ./utils/requirements.txt
start /b python main.py

:: Open Grafana
echo [STEP 6/6] Opening Grafana...
start http://localhost:3000

@pause