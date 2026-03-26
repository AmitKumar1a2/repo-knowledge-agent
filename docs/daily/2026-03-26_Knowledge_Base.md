# Knowledge Base - 2026-03-26

## Q: What is the difference between MMR and plain similarity search in a RAG pipeline?
**A:** Plain similarity search returns the nearest matches by score, which can produce redundant chunks. MMR trades a small amount of raw similarity for diversity, making retrieved context more likely to cover distinct aspects of the query.

**Type:** CONCEPTUAL
**Tags:** rag, retrieval, mmr, similarity-search
**Source:** codex conversation

---

## Q: Why use MCP instead of relying only on raw prompts?
**A:** MCP gives the model a structured interface to tools, context, and external systems instead of encoding everything inside long prompts. That improves reliability, reduces prompt sprawl, and makes workflows easier to standardize across repeated tasks.

**Type:** CONCEPTUAL
**Tags:** mcp, agent-design, prompting, tooling
**Source:** codex conversation

---
