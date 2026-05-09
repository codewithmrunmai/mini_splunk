# Quick Reference - Mini Splunk

## One-Time Setup

### macOS
```bash
brew install --cask docker
brew install ollama
ollama serve
ollama pull llama2
```

### Windows
```powershell
# Install Docker Desktop: https://www.docker.com/products/docker-desktop
# Install Ollama: https://ollama.ai/download
ollama serve
ollama pull llama2
```

---

## Start Application (Both Platforms)

```bash
cd mini_splunk/infra
docker-compose up --build -d
```

**Access:** http://localhost:3000

---

## Common Commands

| Task | Command |
|------|---------|
| **Start services** | `docker-compose up -d` |
| **Stop services** | `docker-compose down` |
| **View logs** | `docker-compose logs -f` |
| **Rebuild** | `docker-compose up --build` |
| **Restart service** | `docker-compose restart <service-name>` |
| **Check status** | `docker ps` |
| **Clean everything** | `docker-compose down -v` |

---

## Service URLs

| Service | URL |
|---------|-----|
| Dashboard | http://localhost:3000 |
| API Gateway | http://localhost:8080 |
| AI Service | http://localhost:8000 |
| Auth Service | http://localhost:8081 |
| Event Service | http://localhost:8082 |
| Detection Service | http://localhost:8083 |

---

## Troubleshooting

**Port conflict:**
```bash
# macOS/Linux
lsof -i :8080

# Windows
netstat -ano | findstr :8080
```

**Services won't start:**
```bash
docker-compose logs <service-name>
docker-compose down -v
docker-compose up --build
```

**Docker not running:**
- Open Docker Desktop application

---

## Project Structure

```
mini_splunk/
├── frontend/           # React (Port 3000)
├── backend/
│   ├── api-gateway/   # Port 8080
│   ├── auth-service/  # Port 8081
│   ├── event-service/ # Port 8082
│   └── detection-service/ # Port 8083
├── ai-service/        # Python (Port 8000)
└── infra/
    └── docker-compose.yml
```

---

For detailed instructions: See **[SETUP.md](SETUP.md)**
