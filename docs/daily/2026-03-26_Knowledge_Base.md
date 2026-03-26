# Knowledge Base - 2026-03-26

## Q: When should you use MMR instead of plain similarity search in a RAG pipeline?
**A:** Use plain similarity search when you want the closest matches only. Use MMR when you also want diversity across retrieved chunks so the context window covers different aspects of the query instead of repeating near-duplicates.

**Type:** CONCEPTUAL
**Tags:** rag, retrieval, mmr, similarity-search
**Source:** cline conversation

---

## Q: Why use MCP instead of relying only on raw prompts?
**A:** MCP gives the model structured access to tools, context, and external systems with clearer boundaries than raw prompting alone. That improves reliability, reduces prompt bloat, and makes repeated workflows easier to standardize.

**Type:** CONCEPTUAL
**Tags:** mcp, agent-design, prompting, tooling
**Source:** cline conversation

---
