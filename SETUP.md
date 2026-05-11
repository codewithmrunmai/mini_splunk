# SentinelAI - Quick Setup Guide

This guide works for both **macOS** and **Windows**.

## Prerequisites

### 1. Install Docker Desktop

#### macOS
```bash
# Option 1: Using Homebrew
brew install --cask docker

# Option 2: Download from
# https://www.docker.com/products/docker-desktop
```

#### Windows
```powershell
# Download and install Docker Desktop from:
# https://www.docker.com/products/docker-desktop

# Enable WSL 2 backend (recommended)
# Follow the installer instructions
```

**Verify Docker Installation:**
```bash
# Same command for both Mac and Windows
docker --version
docker-compose --version
```

### 2. Install Ollama (Optional - for AI features)

#### macOS
```bash
# Install Ollama
brew install ollama

# Start Ollama service
ollama serve

# In a new terminal, pull the model
ollama pull llama2
```

#### Windows
```powershell
# Download from: https://ollama.ai/download
# Run the installer

# After installation, in Command Prompt or PowerShell:
ollama serve

# In a new terminal:
ollama pull llama2
```

**Verify Ollama:**
```bash
# Same for both platforms
curl http://localhost:11434
```

### 3. Install Git (if not already installed)

#### macOS
```bash
brew install git
```

#### Windows
```powershell
# Download from: https://git-scm.com/download/win
```

---

## Quick Setup

### Step 1: Clone or Navigate to Project

```bash
# If cloning from repository
git clone <repository-url>
cd sentinelai

# Or just navigate to the project directory
cd /path/to/sentinelai
```

### Step 2: Navigate to Infrastructure Directory

**macOS/Linux:**
```bash
cd infra
```

**Windows (Command Prompt):**
```cmd
cd infra
```

**Windows (PowerShell):**
```powershell
cd infra
```

### Step 3: Start All Services

**Both macOS and Windows:**
```bash
docker-compose up --build
```

**To run in background (detached mode):**
```bash
docker-compose up --build -d
```

This single command will:
- ✅ Build all 4 Spring Boot microservices
- ✅ Build Python AI service
- ✅ Build React frontend
- ✅ Start PostgreSQL database
- ✅ Start Kafka + Zookeeper
- ✅ Start all 6 application services

**Build time:** 5-10 minutes (first time only)

### Step 4: Access the Application

Once all services are running, open your browser:

- **Frontend Dashboard:** http://localhost:3000
- **API Gateway:** http://localhost:8080
- **AI Service:** http://localhost:8000

---

## Service Ports

| Service | Port | URL |
|---------|------|-----|
| Frontend (React) | 3000 | http://localhost:3000 |
| API Gateway | 8080 | http://localhost:8080 |
| Auth Service | 8081 | http://localhost:8081 |
| Event Service | 8082 | http://localhost:8082 |
| Detection Service | 8083 | http://localhost:8083 |
| AI Service (Python) | 8000 | http://localhost:8000 |
| PostgreSQL | 5432 | - |
| Kafka | 9092 | - |

---

## Common Commands

### Check Running Services

**Both platforms:**
```bash
docker ps
```

### View Logs

**All services:**
```bash
docker-compose logs
```

**Follow logs in real-time:**
```bash
docker-compose logs -f
```

**Specific service:**
```bash
docker-compose logs -f api-gateway
docker-compose logs -f auth-service
docker-compose logs -f event-service
docker-compose logs -f detection-service
docker-compose logs -f ai-service
docker-compose logs -f frontend
```

### Stop Services

**Both platforms:**
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

### Restart Services

**Both platforms:**
```bash
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart auth-service
```

### Rebuild After Code Changes

**Both platforms:**
```bash
# Rebuild all services
docker-compose up --build

# Rebuild specific service
docker-compose up --build api-gateway
```

---

## Troubleshooting

### Issue 1: Port Already in Use

**Error:** `Port 8080 is already allocated`

**macOS/Linux:**
```bash
# Find process using the port
lsof -i :8080

# Kill the process
kill -9 <PID>
```

**Windows (PowerShell):**
```powershell
# Find process using the port
netstat -ano | findstr :8080

# Kill the process
taskkill /PID <PID> /F
```

### Issue 2: Docker Not Running

**Error:** `Cannot connect to the Docker daemon`

**Solution:** Start Docker Desktop application

### Issue 3: Build Fails

**Solution:**
```bash
# Clean everything and rebuild
docker-compose down -v
docker system prune -a
docker-compose up --build
```

### Issue 4: Ollama Connection Issues (AI Service)

**macOS/Linux:**
```bash
# Verify Ollama is running
curl http://localhost:11434

# Check if model is downloaded
ollama list

# Pull model if missing
ollama pull llama2
```

**Windows:**
```powershell
# Verify Ollama is running
curl http://localhost:11434

# Check if model is downloaded
ollama list

# Pull model if missing
ollama pull llama2
```

### Issue 5: Services Keep Restarting

**Check logs:**
```bash
docker-compose logs <service-name>
```

**Common causes:**
- Database connection issues
- Port conflicts
- Memory issues (increase Docker memory in Docker Desktop settings)

---

## Platform-Specific Notes

### macOS Specific

**Ollama Host Access:**
- Docker can access host machine via `http://host.docker.internal:11434`
- This is already configured in the AI service

**M1/M2 (Apple Silicon):**
- All images support ARM architecture
- No additional configuration needed

### Windows Specific

**WSL 2 Backend (Recommended):**
- Enable WSL 2 in Docker Desktop settings
- Better performance and compatibility

**Ollama Host Access:**
- Docker can access host machine via `http://host.docker.internal:11434`
- This is already configured in the AI service

**Path Differences:**
- Use forward slashes `/` in docker-compose.yml (already done)
- Git bash recommended for better compatibility with Unix commands

---

## Quick Start Summary

### macOS
```bash
# 1. Install prerequisites
brew install --cask docker
brew install ollama

# 2. Start Ollama (optional)
ollama serve
ollama pull llama2  # in new terminal

# 3. Navigate and start
cd sentinelai/infra
docker-compose up --build -d

# 4. Open browser
open http://localhost:3000
```

### Windows (PowerShell)
```powershell
# 1. Install Docker Desktop and Ollama manually
# https://www.docker.com/products/docker-desktop
# https://ollama.ai/download

# 2. Start Ollama (optional)
ollama serve
ollama pull llama2  # in new terminal

# 3. Navigate and start
cd sentinelai\infra
docker-compose up --build -d

# 4. Open browser
start http://localhost:3000
```

---

## Stopping the Application

**Both platforms:**
```bash
cd infra
docker-compose down
```

**Complete cleanup (removes volumes):**
```bash
docker-compose down -v
```

---

## System Requirements

- **RAM:** 8GB minimum, 16GB recommended
- **Storage:** 10GB free space (for Docker images)
- **CPU:** 4 cores recommended
- **Docker Desktop:** Latest version

---

## What's Included

This boilerplate template includes:

✅ **Frontend:** React dashboard (http://localhost:3000)  
✅ **API Gateway:** Spring Cloud Gateway  
✅ **Auth Service:** JWT authentication (template)  
✅ **Event Service:** Kafka producer (template)  
✅ **Detection Service:** Kafka consumer (template)  
✅ **AI Service:** FastAPI + Ollama integration  
✅ **Database:** PostgreSQL  
✅ **Message Queue:** Apache Kafka + Zookeeper  
✅ **Containerization:** Complete Docker setup  

All services are **running** but have minimal functionality (TODOs). This is a starting template for development.

---

## Next Steps

1. ✅ Services are running
2. 📝 Implement TODOs in each service
3. 🔧 Add entities, controllers, and business logic
4. 🎨 Build out the frontend components
5. 🤖 Connect AI service to Ollama for analysis

Happy coding! 🚀
