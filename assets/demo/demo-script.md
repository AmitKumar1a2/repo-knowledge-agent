# Demo Script

## Goal

Show how a conceptual conversation becomes reusable repo-native knowledge.

## Demo Flow

1. Start in the repository with the existing Codex or Cline setup.
2. Ask:

```text
Explain MMR vs similarity search in RAG
```

3. Show that the request is treated as conceptual learning rather than implementation work.
4. Show the knowledge entry being written to:

```text
docs/daily/YYYY-MM-DD_Knowledge_Base.md
```

5. Open the daily file and show the structured output:

```md
## Q: What is the difference between MMR and plain similarity search in a RAG pipeline?
**A:** Plain similarity search returns the nearest matches by score, which can produce redundant chunks. MMR trades a small amount of raw similarity for diversity, making retrieved context more likely to cover distinct aspects of the query.

**Type:** CONCEPTUAL
**Tags:** rag, retrieval, mmr, similarity-search
**Source:** codex conversation
```

6. Highlight that the result is stored locally, readable in git, and reusable later.
