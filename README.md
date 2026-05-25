# 🤖 AI Customer Support Agent (customer_support_llm)

An end-to-end, production-style AI customer support agent for e-commerce. Built from scratch using an incremental "stack-upon-stack" approach — starting from a raw LLM call and progressively adding RAG, memory, intent classification, order tracking, returns processing, live web scraping, and deployment.

> **Status:** 🚧 In active development (25-day build plan)

---

## 📸 Demo

*Coming soon — end-to-end demo video after Day 25*

---

## ✨ Features

- **RAG-powered product Q&A** — Answers product questions using a vector knowledge base (ingredients, usage, side effects)
- **Conversational memory** — Maintains context across multi-turn dialogues
- **Intent classification** — Detects `track_order`, `return`, `refund`, `product_query` intents
- **Order tracking & returns** — Queries a live database and processes returns with verification
- **Live web scraping** — Fetches real-time prices, discounts, and coupons from the store website
- **Fallback to human** — Escalates to email when the bot can't handle a query
- **Chat widget embed** — Drop-in JavaScript widget for any e-commerce store
- **Multi-tenancy** — Supports multiple stores with isolated knowledge bases
- **Admin dashboard** — Store owners can upload docs, view analytics, and manage the bot
- **100% local-first** — Runs entirely on Ollama (Mistral) during development — zero API costs

---

## 🛠 Tech Stack

| Layer | Technology |
|:--|:--|
| **LLM** | Ollama + Mistral 7B (local, free) |
| **Orchestration** | LangChain |
| **Vector Store** | ChromaDB |
| **Embeddings** | OllamaEmbeddings |
| **Memory** | Redis |
| **Backend API** | FastAPI |
| **Frontend** | Streamlit + Custom JS Widget |
| **Database** | SQLite |
| **Scraping** | BeautifulSoup4 + Playwright |
| **Containerization** | Docker |
| **Monitoring** | Custom logging + Streamlit dashboard |

---

## 📅 25-Day Build Plan

This project follows a strict incremental build philosophy: **one feature per day, each building on the last.**

| Phase | Days | Focus |
|:--|:--|:--|
| **Foundation** | 1–5 | LLM setup, LangChain, RAG pipeline |
| **Intelligence** | 6–9 | Memory, citations, intent classification |
| **Actions** | 10–13 | Database access, order tracking, returns |
| **Live Data** | 14–16 | Web scraping, live info injection |
| **Production** | 17–22 | Email fallback, FastAPI, Redis, widget, Docker |
| **Polish** | 23–25 | Monitoring, admin dashboard, testing |

📋 **[Interactive Checklist](https://github.com/Ashaiky36/customer-support-llm/AICSA_CHECKLIST.html)** — Track your progress with persistent checkboxes and a progress bar.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) installed
- Mistral model pulled: `ollama pull mistral`
- Redis (for Day 19+)

### Installation

```bash
# Clone the repo
git clone https://github.com/Ashaiky36/customer_support_llm.git
cd customer-support-llm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull the model
ollama pull mistral