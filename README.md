# 🤖 AI Ticket Summarizer

A production-ready, full-stack application that transforms complex, messy support chat logs into professional, structured "AI Overviews." Built with a stateless FastAPI backend, a modern React frontend, and fully containerized with Docker.

## � Prerequisites

Before you begin, ensure you have the following installed:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
- An [OpenAI API Key](https://platform.openai.com/api-keys)

## �🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/aditya2812/ai-ticket-summarizer.git
cd ai-ticket-summarizer
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```env
OPENAI_API_KEY=your_sk_key_here
```

### 3. Launch with Docker
```bash
docker compose up -d
```

Your app is now running at:
- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Technology Stack

| Layer | Technology | Usage |
| :--- | :--- | :--- |
| **Frontend** | React + Vite | Fast, responsive UI with real-time AI loading states. |
| **Backend** | FastAPI | High-performance Python API with automatic OpenAPI docs. |
| **AI Engine** | OpenAI SDK | GPT-4o-mini for intelligent text summarization. |
| **Database** | PostgreSQL 15 | Persistent storage for processed ticket summaries. |
| **ORM** | SQLAlchemy | Pythonic database management and migrations. |
| **DevOps** | Docker Compose | Multi-container orchestration for seamless deployment. |

---

## 🏗️ System Architecture

The application uses a **Stateless Microservice** architecture:
1. **Frontend (Vite/React)** captures raw ticket text and sends an HTTP POST to the backend.
2. **Backend (FastAPI)** validates the data using Pydantic schemas.
3. **AI Service** processes the text using a refined system prompt for root-cause analysis.
4. **Database (Postgres)** stores the final "Analyze" result for auditing.
5. **Docker** ensures the entire environment is identical across development and production.

---

## 📊 Useful Docker Commands

- **Check container health**: `docker compose ps`
- **View backend logs**: `docker compose logs -f backend`
- **Reset database volume**: `docker compose down -v && docker compose up -d`
- **Inspect DB records**: `docker compose exec -it db psql -U postgres_user -d postgres_db`

---

## 📄 License
This project is open-source and available under the MIT License.
