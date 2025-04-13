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

<pre> <code> ``` QueryBaseAI/ ├── Backend/ # Django logic (views, serializers, APIs) ├── Core/ # Core database logics ├── LLM/ # LLM providers (OpenAI & AI21 logic) ├── ExternalTools/ # Elastic, Milvus connectors ├── .env # Environment variables └── README.md # Project documentation ``` </code> </pre>

---
