# SentinelAI - Intelligent Log Monitoring System

A microservices-based log aggregation and analysis platform with AI-powered insights.

## Architecture

```
Frontend (React) → API Gateway → Microservices
                                      ↓
                                   Kafka
                                      ↓
                            AI Analysis Service
```

## Services

- **Frontend**: React dashboard (Port 3000)
- **API Gateway**: Spring Boot Gateway (Port 8080)
- **Auth Service**: Authentication & JWT (Port 8081)
- **Event Service**: Log ingestion (Port 8082)
- **Detection Service**: Log analysis (Port 8083)
- **AI Service**: Python FastAPI AI analysis (Port 8000)

## Tech Stack

- Frontend: React
- Backend: Spring Boot, Spring Cloud Gateway, Kafka
- AI Service: Python FastAPI + Ollama
- Database: PostgreSQL
- Message Queue: Apache Kafka
- Container: Docker + Docker Compose

## Quick Start

**Works on both macOS and Windows!**

### Prerequisites
- Docker Desktop
- Git
- Ollama (optional, for AI features)

### Setup Commands

```bash
# Navigate to project
cd sentinelai/infra

# Start all services (macOS/Windows)
docker-compose up --build -d

# Access dashboard
# macOS: open http://localhost:3000
# Windows: start http://localhost:3000
# Or just visit http://localhost:3000 in your browser
```

**📖 For detailed setup instructions, see [SETUP.md](SETUP.md)**

## Project Structure

```
sentinelai/
├── frontend/              # React frontend
├── backend/
│   ├── api-gateway/      # API Gateway
│   ├── auth-service/     # Authentication
│   ├── event-service/    # Event/Log ingestion
│   └── detection-service/# Log analysis
├── ai-service/           # AI analysis service
└── infra/                # Docker compose
```

## Development

This is a template project. Implement the TODOs in each service to build functionality.
