@echo off
REM Zep Memory Assistant - Startup Script
REM This script ensures the app runs in the 'agentic' conda environment

echo ========================================
echo   Zep Memory Assistant
echo ========================================
echo.

REM Check if Ollama is running
echo [1/3] Checking Ollama status...
curl -s http://127.0.0.1:11434/api/version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Ollama is not running!
    echo Please start Ollama in a separate terminal:
    echo    ollama serve
    echo.
    pause
    exit /b 1
)
echo [OK] Ollama is running
echo.

REM Check if qwen3:4b model exists
echo [2/3] Checking if qwen3:4b model is available...
ollama list | findstr "qwen3:4b" >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] qwen3:4b model not found!
    echo Pulling the model now (this may take a few minutes)...
    ollama pull qwen3:4b
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to pull model
        pause
        exit /b 1
    )
)
echo [OK] qwen3:4b model is available
echo.

REM Start the Streamlit app in the agentic environment
echo [3/3] Starting Zep Memory Assistant...
echo Running in 'agentic' conda environment
echo.
echo ========================================
echo   App will open in your browser
echo   Press Ctrl+C to stop the app
echo ========================================
echo.

REM Use conda run to ensure correct environment
conda run -n agentic streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to start the app
    echo Make sure the 'agentic' conda environment exists and has all dependencies
    echo.
    pause
)
