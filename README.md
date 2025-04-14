## 🚀 QueryBaseAI

An AI-powered hybrid search engine combining **Keyword Search**, **Vector Similarity Search**, and **LLM-based contextual answers** using **Retrieval Augmented Generation (RAG)** via **AI21**, **OpenAI** or any other LLM.

---

## 🧠 Overview

**QueryBaseAI** lets users create organisations, upload documents, automatically chunk & index them using Elasticsearch and Milvus, and ask natural language queries. The system generates smart, contextual answers using **RAG** powered by **AI21 or OpenAI** (configurable).

---

## 🔧 Tech Stack

| Layer         | Stack                                  |
|---------------|----------------------------------------|
| Backend       | Django, Django REST Framework (DRF)    |
| LLMs          | AI21 & OpenAI (via user config)        |
| Vector Store  | Milvus                                 |
| Text Search   | Elasticsearch                          |
| Logging       | Logstash, Kibana (ELK Stack)           |
| Orchestration | Docker, Docker Compose                 |

---

## 💡 Key Features

- 📄 Upload multi-format docs (PDF, DOCX, TXT, MD)
- 🔗 Chunking, indexing & hybrid retrieval (keyword + vector)
- 🧠 Answer generation using **RAG** with OpenAI or AI21
- 📦 Dockerized microservices (Milvus, Elastic, Kibana)
- 📊 Real-time centralized logging (ELK stack)

---

## 📁 Project Structure

```
QueryBaseAI/
├── Backend/           # Django logic (views, serializers, APIs)
├── Core/              # Core database logics
├── LLM/               # LLM providers (OpenAI & AI21 logic)
├── ExternalTools/     # Elastic, Milvus connectors
├── .env               # Environment variables
└── README.md          # Project documentation
```

---

## 💻 Getting Started

1. Clone the repository from GitHub to your local machine
```bash
git clone https://github.com/GoodGuyAdy/QueryBaseAI.git
```
2. Change the current directory to the cloned project folder
```bash
cd QueryBaseAI
```
3. Install the Python dependencies listed in the requirements.txt file
```bash
pip install -r requirements.txt
```
4. Build and starts the Docker containers defined in the docker-compose.yml file
```bash
docker-compose up --build
```
5. Run the Django development server for the project
```bash
python manage.py runserver
```

---

## 🧑🏻‍🔧 Troubleshooting :-
 
 - Ensure that your .env file contains a valid OPENAI_API_KEY or AI21_API_KEY.
 - Make sure you have an active internet connection.

---
