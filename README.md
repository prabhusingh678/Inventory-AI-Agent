inventory-ai-agent/
│
├── backend/
│   ├── app/
│   │   ├── main.py              
│   │   ├── agent.py             
│   │   ├── db.py                
│   │   ├── tools.py            
│   │   └── llm.py               
│   ├── init.sql                
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│   └── Dockerfile
│
├── fine_tuning/
│   ├── train.py
│   ├── dataset.json
│   └── README.md
│
├── docker-compose.yml
├── README.md
└── .gitignore





  Inventory AI Agent

# Overview
AI-powered system to query and manage warehouse inventory using natural language.

---

##  Architecture

Browser → FastAPI → Agent → Database → Response

---

##  Setup

### 1. Clone
git clone https://github.com/yourusername/inventory-ai-agent.git

### 2. Run
docker-compose up --build -d

### 3. Open
Frontend → http://localhost:3000  
Backend → http://localhost:8000  

---

##  Example Queries
- "List all items"
- "Which items are low in stock?"

---

##  Design Choices

### LLM
OpenAI GPT model for simplicity and accuracy.

### Database
PostgreSQL for structured inventory data.

### Agent
Custom lightweight agent for tool-calling.

### Trade-offs
- Simplicity over heavy frameworks
- Faster development vs full LangChain pipeline

---

##  Fine-Tuning
See `/fine_tuning` folder.

---

##  Docker
Fully containerized using docker-compose.
