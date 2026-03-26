# 🚀 Repo Knowledge Agent (RKCA)

> Turn developer conversations into structured, searchable knowledge — automatically.

---

## 🧠 What is this?

**Repo Knowledge Agent (RKCA)** is a **Cline-first, repo-native agent system** that captures *conceptual learning* from AI conversations and stores it as a structured knowledge base inside your repository.

Instead of losing context in chats, RKCA converts insights into reusable documentation — automatically.

---

## ⚡ Why this exists

Developers today:

- Learn through AI conversations (Cline, Codex, ChatGPT)
- Solve problems fast… but forget context just as fast
- Rarely document learnings
- Revisit the same concepts repeatedly

👉 RKCA solves this by turning **thinking → memory → knowledge**

---

## 🔥 What it does

RKCA sits inside your repo and:

- 🧠 **Classifies conversations** → Conceptual vs Implementation  
- 📝 **Captures only meaningful learning** (not noise)  
- 🔄 **Rewrites into reusable Q&A format**  
- 🗂️ **Stores knowledge daily inside your repo**  
- 🏷️ **Tags for future retrieval**

---

## 🏗️ How it works

User → Cline → RKCA Rules → Classifier → If Conceptual → Store in docs/daily/

---

## 📂 Project Structure

repo-knowledge-agent/
│
├── .clinerules/
├── scripts/
├── docs/
│   └── daily/
└── README.md

---

## 🧩 Example Output

# Knowledge Base - 2026-03-26

## Q: What is the difference between MMR and similarity search in RAG?
**A:** Similarity search retrieves top-k closest vectors purely by distance, which can result in redundant chunks. MMR balances relevance with diversity.

**Type:** CONCEPTUAL  
**Tags:** rag, embeddings, retrieval  
**Source:** cline conversation  

---

## 🧠 Design Philosophy

This is not a prompt.  
This is a **developer memory system**.

---

## 🚀 Roadmap

- Semantic duplicate detection
- Weekly summaries
- MCP integration
- Codex skill packaging

---

## ⭐ If this helped you

Give it a star ⭐
