# AI Customer Support Agent — Production-Grade RAG System

An end-to-end AI-powered customer support system designed for e-commerce platforms. The agent handles product inquiries, order tracking, returns processing, and live data retrieval through a modular, incrementally-built architecture. Developed using Retrieval-Augmented Generation (RAG), intent classification, and multi-tenant deployment patterns.

> **Status:** Under active development. Following a structured 25-day build pipeline.

---

## Overview

Modern e-commerce operations require scalable, intelligent support systems capable of handling high volumes of customer interactions without sacrificing accuracy or reliability. This project implements a complete AI support agent that integrates natural language understanding, structured knowledge retrieval, transactional database access, and live web scraping into a unified, deployable system.

The development follows a disciplined incremental methodology: each phase introduces a single new capability onto a stable foundation, ensuring thorough understanding of every component before integration.

---

## Core Capabilities

- **Retrieval-Augmented Generation (RAG)** — Product knowledge base ingestion, chunking, embedding, vector storage, and semantic retrieval for accurate, source-grounded responses
- **Conversational State Management** — Multi-turn dialogue memory with persistent session storage
- **Intent Classification** — Structured extraction of user intents including product inquiry, order tracking, return initiation, and refund requests
- **Transactional Operations** — SQL database querying for order status verification, return eligibility checks, and delivery tracking
- **Live Data Enrichment** — Web scraping pipeline for real-time product pricing, availability, discounts, and coupon retrieval
- **Human Escalation Protocol** — Automated email fallback when queries exceed the agent's confidence threshold or operational scope
- **Embeddable Interface** — Standalone JavaScript widget for integration into existing e-commerce storefronts
- **Multi-Tenant Architecture** — Isolated vector stores and configurations per store, enabling SaaS deployment
- **Observability Dashboard** — Administrative interface for conversation monitoring, analytics review, and knowledge base management
- **Local-First Development** — All LLM inference performed locally via Ollama, eliminating external API dependency during development

---

## Technical Architecture

| Component | Implementation |
|:--|:--|
| Language Model | Ollama (Mistral 7B) — local inference |
| Orchestration Framework | LangChain |
| Vector Database | ChromaDB |
| Embedding Model | OllamaEmbeddings |
| Session Store | Redis |
| API Layer | FastAPI |
| Frontend Interface | Streamlit / Custom JavaScript Widget |
| Transactional Database | SQLite |
| Web Scraping | BeautifulSoup4 / Playwright |
| Containerization | Docker |
| Observability | Structured logging + Custom Streamlit dashboard |

---

## Incremental Development Pipeline

The system is constructed over 25 sequential development phases, organized into six logical stages:

| Stage | Days | Scope |
|:--|:--|:--|
| Foundation | 1–5 | LLM integration, prompt engineering, document processing, vector storage, RAG pipeline |
| Intelligence | 6–9 | Conversational memory, source citation, confidence thresholds, intent classification |
| Transactional Layer | 10–13 | Database schema design, SQL generation from natural language, order tracking, return verification |
| Live Data Integration | 14–16 | Static and dynamic web scraping, real-time context injection into RAG pipeline |
| Production Hardening | 17–22 | API development, persistent sessions, widget embedding, multi-tenancy, containerization |
| Operational Readiness | 23–25 | Structured logging, cost tracking, administrative dashboard, end-to-end testing |

A detailed interactive checklist with progress tracking is available in the repository.

---

## Installation

### Prerequisites

- Python 3.10 or later
- Ollama installed and running locally
- Mistral model: `ollama pull mistral`
- Redis server (required from Day 19 onward)

### Setup

```bash
git clone https://github.com/Ashaiky36/customer_support_llm.git
cd ai-support-agent

python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

pip install -r requirements.txt
ollama pull mistral