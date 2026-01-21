# 🚀 Zep Memory Assistant - Complete Setup Guide

This guide will walk you through **every step** needed to get the Zep Memory Assistant running on your machine, including where to get API keys and how to configure them.

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [API Keys Required](#api-keys-required)
3. [Step-by-Step Installation](#step-by-step-installation)
4. [Running the Project](#running-the-project)
5. [Verification Steps](#verification-steps)
6. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

Before starting, ensure you have:

- **Windows 10/11** (or Linux/macOS)
- **Python 3.12 or higher** installed
- **Internet connection** (for downloading models and API access)
- **4GB+ RAM** available (for running the LLM locally)
- **5GB+ disk space** (for Ollama and models)

### Check Python Version

```powershell
python --version
```

**Expected output**: `Python 3.12.x` or higher

> ⚠️ If Python version is lower than 3.12, download and install from [python.org](https://www.python.org/downloads/)

---

## 🔑 API Keys Required

This project requires **ONE API key**:

### 1. Zep Cloud API Key

**What it's for**: Long-term memory storage and retrieval for the AI agent

**Where to get it**:

#### Step 1: Create Zep Account
1. Visit **[https://www.getzep.com/](https://www.getzep.com/)**
2. Click **"Get Started"** or **"Sign Up"**
3. Choose one of these sign-up methods:
   - Sign up with **Google**
   - Sign up with **GitHub**
   - Sign up with **Email**

#### Step 2: Access Dashboard
1. After signing up, you'll be redirected to the Zep dashboard
2. URL will be: **[https://app.getzep.com/](https://app.getzep.com/)**

#### Step 3: Get API Key
1. In the dashboard, look for **"API Keys"** in the left sidebar
2. Click **"Create API Key"** or **"Generate New Key"**
3. Give it a name (e.g., "Zep Memory Assistant")
4. Click **"Create"**
5. **COPY THE API KEY IMMEDIATELY** - it will look like:
   ```
   z_1dWlkIjoiMjU1NDQ2NTYtNmZkNC00MDhlLTllNzYtMTkzZjM2ZDdhZDUwIn0.hxR_uzmQYUnKJyiyW8jxAen6FLgMRQpEjMGjXecW3IzdEagoASCaQu8ON2d6R6nXR38EbyKg3xELaLq9jl5nbw
   ```
6. **⚠️ IMPORTANT**: Save this key somewhere safe! You won't be able to see it again.

#### Step 4: Save Your API Key
Create a text file to store it temporarily:
```powershell
# Create a file to store your API key (DO NOT commit this to git!)
notepad api_keys.txt
```

Paste your key in this format:
```
ZEP_API_KEY=z_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Free Tier Limits**:
- ✅ 1,000 messages per month
- ✅ 100 users
- ✅ 30-day message retention
- ✅ All core features

> 💡 **Tip**: The free tier is more than enough for testing and personal use!

---

## 🛠️ Step-by-Step Installation

### Step 1: Install Ollama (Local LLM Server)

Ollama runs the AI model locally on your machine (no cloud API needed).

#### For Windows:

1. **Download Ollama**:
   - Visit **[https://ollama.com/download](https://ollama.com/download)**
   - Click **"Download for Windows"**
   - Download the `.exe` installer

2. **Install Ollama**:
   - Run the downloaded `OllamaSetup.exe`
   - Follow the installation wizard
   - Click **"Install"** and wait for completion

3. **Verify Installation**:
   ```powershell
   ollama --version
   ```
   
   **Expected output**:
   ```
   ollama version is 0.x.x
   ```

4. **Start Ollama** (it usually starts automatically):
   ```powershell
   # Check if Ollama is running
   curl http://127.0.0.1:11434/api/version
   ```
   
   **Expected output**: JSON response with version info

   **If not running**, start it manually:
   ```powershell
   ollama serve
   ```

#### For Linux/macOS:

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Verify installation
ollama --version
```

---

### Step 2: Download the AI Model

We use **Qwen 3 (4B parameter model)** - it's efficient and runs well on most machines.

```powershell
# Pull the Qwen 3 model (this will download ~2.3 GB)
ollama pull qwen3:4b
```

**What you'll see**:
```
pulling manifest
pulling 8b9c8f8... 100% ▕████████████████▏ 2.3 GB
pulling 4b8c9e... 100% ▕████████████████▏ 1.5 KB
...
success
```

**Verify the model is installed**:
```powershell
ollama list
```

**Expected output**:
```
NAME            ID              SIZE      MODIFIED
qwen3:4b        abc123def456    2.3 GB    2 minutes ago
```

**Test the model** (optional but recommended):
```powershell
ollama run qwen3:4b "Hello, how are you?"
```

You should get a response from the model. Press `Ctrl+D` or type `/bye` to exit.

---

### Step 3: Clone/Navigate to Project Directory

```powershell
# Navigate to your project directory
cd "a:\shinobi no shuriken\github repo\agentic system_\zep-memory-assistant"

# Verify you're in the right directory
dir
```

**You should see these files**:
```
app.py
agent.py
prompt.py
llm_config.py
util.py
pyproject.toml
README.md
```

---

### Step 4: Install Python Dependencies

#### Option A: Using `uv` (Recommended - Faster)

```powershell
# Install uv if you don't have it
pip install uv

# Install all dependencies
uv sync
```

**What this does**:
- Reads `pyproject.toml`
- Installs all required packages
- Creates a virtual environment automatically

#### Option B: Using `pip` (Traditional Method)

```powershell
# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install "ag2[ollama]>=0.9" "ollama>=0.4.8" "streamlit>=1.44.1" "zep-cloud>=2.11.0"
```

**Verify installation**:
```powershell
pip list
```

**You should see**:
```
ag2                 0.9.x
ollama              0.4.x
streamlit           1.44.x
zep-cloud           2.11.x
... (and their dependencies)
```

---

### Step 5: Configure Environment (Optional)

While the app accepts API keys through the UI, you can optionally set them as environment variables.

#### Create `.env` file (Optional):

```powershell
# Create .env file
notepad .env
```

Add this content:
```env
# Zep Configuration
ZEP_API_KEY=z_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Ollama Configuration (default values, usually no need to change)
OLLAMA_HOST=http://127.0.0.1:11434
OLLAMA_MODEL=qwen3:4b
```

> ⚠️ **IMPORTANT**: Add `.env` to your `.gitignore` to avoid committing secrets!

```powershell
# Create/update .gitignore
echo .env >> .gitignore
echo api_keys.txt >> .gitignore
```

---

## ▶️ Running the Project

### Start the Application

```powershell
# Make sure you're in the project directory
cd "a:\shinobi no shuriken\github repo\agentic system_\zep-memory-assistant"

# Run the Streamlit app
streamlit run app.py
```

**What you'll see**:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**The app will automatically open in your default browser!**

If it doesn't open automatically:
1. Copy the URL: `http://localhost:8501`
2. Paste it in your browser

---

## 🎯 First-Time Setup in the App

### Step 1: Enter Zep API Key

1. Look at the **left sidebar** in the app
2. Find the **"Zep API Key"** input field
3. Paste your Zep API key (starts with `z_`)
4. Click outside the input field or press Enter

**You should see**:
```
✅ Zep client initialized successfully
```

**If you see an error**:
- ❌ Check that you copied the entire API key
- ❌ Verify your internet connection
- ❌ Make sure the API key hasn't been revoked

---

### Step 2: Enter Your Information

1. In the sidebar, find **"User Information"** section
2. Enter your **First Name** (e.g., "John")
3. Enter your **Last Name** (e.g., "Smith")
4. Click **"Initialize Session ✅"**

**You should see**:
```
✅ Zep user/session initialized successfully
```

**Session Details will appear**:
```
Session ID: 12ab34cd...
User ID: johnsmith
```

---

### Step 3: Start Chatting!

1. At the bottom of the page, you'll see a chat input
2. Type your first message (e.g., "Hello! I'm working on a Python project.")
3. Press **Enter**

**The agent will**:
- Show "Thinking..." briefly
- Generate a response using the Qwen 3 model
- Remember this conversation for future sessions!

---

## ✅ Verification Steps

### 1. Verify Ollama is Running

```powershell
# Check Ollama status
curl http://127.0.0.1:11434/api/version
```

**Expected**: JSON response with version

**If failed**:
```powershell
# Start Ollama
ollama serve
```

---

### 2. Verify Model is Available

```powershell
ollama list
```

**Expected**: `qwen3:4b` in the list

**If missing**:
```powershell
ollama pull qwen3:4b
```

---

### 3. Verify Python Dependencies

```powershell
python -c "import streamlit; import zep_cloud; import autogen; print('All imports successful!')"
```

**Expected**: `All imports successful!`

**If failed**:
```powershell
# Reinstall dependencies
pip install "ag2[ollama]>=0.9" "ollama>=0.4.8" "streamlit>=1.44.1" "zep-cloud>=2.11.0"
```

---

### 4. Verify Zep Connection

In the Streamlit app:
1. Enter your Zep API key
2. Look for: `✅ Zep client initialized successfully`

**If failed**:
- Check API key is correct
- Verify internet connection
- Visit [status.getzep.com](https://status.getzep.com) for service status

---

### 5. Test End-to-End

1. Initialize session with your name
2. Send a message: "Remember that I love Python programming"
3. Clear the chat (click "Clear ↺")
4. Send another message: "What do you know about me?"
5. **The agent should remember** your Python preference!

---

## 🐛 Troubleshooting

### Issue 1: "Ollama connection failed"

**Symptoms**:
- App shows connection errors
- Responses timeout

**Solutions**:

```powershell
# Check if Ollama is running
curl http://127.0.0.1:11434/api/version

# If not running, start it
ollama serve

# In a new terminal, verify it's working
ollama run qwen3:4b "test"
```

---

### Issue 2: "Failed to initialize Zep Client"

**Symptoms**:
- Red error message in sidebar
- Can't initialize session

**Solutions**:

1. **Verify API Key**:
   - Check for typos
   - Ensure you copied the entire key
   - Key should start with `z_`

2. **Check Internet Connection**:
   ```powershell
   ping app.getzep.com
   ```

3. **Regenerate API Key**:
   - Go to [app.getzep.com](https://app.getzep.com)
   - Delete old key
   - Create new key
   - Use the new key in the app

---

### Issue 3: "Model not found"

**Symptoms**:
- Error about `qwen3:4b` not found
- Inference fails

**Solutions**:

```powershell
# List available models
ollama list

# If qwen3:4b is missing, pull it
ollama pull qwen3:4b

# Verify it's downloaded
ollama list
```

---

### Issue 4: "Import errors" or "Module not found"

**Symptoms**:
- Python can't find `streamlit`, `zep_cloud`, or `autogen`

**Solutions**:

```powershell
# Reinstall all dependencies
pip install --force-reinstall "ag2[ollama]>=0.9" "ollama>=0.4.8" "streamlit>=1.44.1" "zep-cloud>=2.11.0"

# Or use uv
uv sync --reinstall
```

---

### Issue 5: Port 8501 already in use

**Symptoms**:
- Error: "Address already in use"
- Can't start Streamlit

**Solutions**:

```powershell
# Option 1: Use a different port
streamlit run app.py --server.port 8502

# Option 2: Kill the process using port 8501
# Find the process
netstat -ano | findstr :8501

# Kill it (replace PID with actual process ID)
taskkill /PID <PID> /F

# Then restart
streamlit run app.py
```

---

### Issue 6: Slow responses

**Symptoms**:
- Agent takes 10+ seconds to respond
- "Thinking..." for a long time

**Causes & Solutions**:

1. **CPU-based inference** (expected on most machines):
   - Qwen 3 4B on CPU: 2-5 seconds is normal
   - For faster responses, use a smaller model or GPU

2. **Ollama overloaded**:
   ```powershell
   # Restart Ollama
   taskkill /IM ollama.exe /F
   ollama serve
   ```

3. **Use a smaller model** (faster but less capable):
   ```powershell
   # Pull a smaller model
   ollama pull qwen3:1.5b
   ```
   
   Then update `llm_config.py`:
   ```python
   config_list = [
       {
           "model": "qwen3:1.5b",  # Changed from qwen3:4b
           "api_type": "ollama",
           "client_host": "http://127.0.0.1:11434",
       }
   ]
   ```

---

### Issue 7: Memory not working

**Symptoms**:
- Agent doesn't remember previous conversations
- Facts not being recalled

**Solutions**:

1. **Verify session is initialized**:
   - Check sidebar shows "Session Details"
   - User ID and Session ID should be visible

2. **Check Zep dashboard**:
   - Visit [app.getzep.com](https://app.getzep.com)
   - Navigate to Users → Sessions
   - Verify messages are being stored

3. **Reinitialize session**:
   - Refresh the page
   - Enter API key again
   - Initialize new session

---

## 🔄 Restarting the Project

If you need to restart everything:

```powershell
# Stop Streamlit (Ctrl+C in the terminal)

# Stop Ollama
taskkill /IM ollama.exe /F

# Restart Ollama
ollama serve

# In a new terminal, restart Streamlit
cd "a:\shinobi no shuriken\github repo\agentic system_\zep-memory-assistant"
streamlit run app.py
```

---

## 📊 System Requirements Summary

| Component      | Minimum            | Recommended          |
| -------------- | ------------------ | -------------------- |
| **Python**     | 3.12               | 3.12+                |
| **RAM**        | 4 GB               | 8 GB+                |
| **Disk Space** | 5 GB               | 10 GB+               |
| **CPU**        | Dual-core          | Quad-core+           |
| **Internet**   | Required for setup | Required for Zep API |

---

## 🎓 Quick Reference

### Start the Project
```powershell
# 1. Start Ollama (if not running)
ollama serve

# 2. In a new terminal, start the app
cd "a:\shinobi no shuriken\github repo\agentic system_\zep-memory-assistant"
streamlit run app.py

# 3. Open browser to http://localhost:8501
# 4. Enter Zep API key
# 5. Initialize session
# 6. Start chatting!
```

### Stop the Project
```powershell
# Stop Streamlit: Ctrl+C in the terminal
# Stop Ollama: Ctrl+C in the Ollama terminal (or leave it running)
```

### Check Status
```powershell
# Check Ollama
curl http://127.0.0.1:11434/api/version

# Check models
ollama list

# Check Python packages
pip list | findstr "streamlit zep-cloud ag2 ollama"
```

---

## 🆘 Getting Help

If you're still stuck:

1. **Check Logs**:
   ```powershell
   # Run with debug logging
   streamlit run app.py --logger.level=debug
   ```

2. **Verify All Components**:
   - ✅ Ollama running
   - ✅ Model downloaded
   - ✅ Python dependencies installed
   - ✅ Zep API key valid
   - ✅ Internet connection active

3. **Common Issues Checklist**:
   - [ ] Ollama is running on port 11434
   - [ ] `qwen3:4b` model is pulled
   - [ ] All Python packages installed
   - [ ] Zep API key is correct and active
   - [ ] No firewall blocking localhost connections

4. **Resources**:
   - [Zep Documentation](https://docs.getzep.com)
   - [Ollama Documentation](https://ollama.com/docs)
   - [Streamlit Documentation](https://docs.streamlit.io)
   - [AG2 Documentation](https://docs.ag2.ai)

---

## ✅ Success Checklist

Before you start using the app, verify:

- [x] Ollama installed and running
- [x] `qwen3:4b` model downloaded
- [x] Python 3.12+ installed
- [x] All dependencies installed (`uv sync` or `pip install`)
- [x] Zep API key obtained from [getzep.com](https://www.getzep.com)
- [x] Streamlit app starts without errors
- [x] Can enter API key and initialize session
- [x] Agent responds to messages
- [x] Memory persists across conversations

---

**🎉 You're all set! Enjoy your AI agent with human-like memory!**

For detailed architecture and logic explanations, see [PROJECT_GUIDE.md](./PROJECT_GUIDE.md).
