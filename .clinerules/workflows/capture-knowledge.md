# Workflow: Capture Knowledge

Use this workflow when you want to manually capture the most reusable conceptual learning from the current Cline context.

Steps
1. Review the current conversation and identify the strongest reusable conceptual takeaway.
2. Classify it as `CONCEPTUAL`, `IMPLEMENTATION`, or `HYBRID`.
3. Stop if the result is `IMPLEMENTATION`.
4. Rewrite the learning as a clean question suitable for a knowledge base.
5. Write a concise reusable answer.
6. Assign 2-5 practical tags.
7. Append the entry to `docs/daily/YYYY-MM-DD_Knowledge_Base.md`.
8. If the daily file does not exist, create it with `# Knowledge Base - YYYY-MM-DD`.
9. If a near-duplicate already exists, merge with the existing knowledge instead of adding a redundant entry. Prefer one stronger entry over two similar ones.

Entry Format

```md
## Q: <clear rewritten question>
**A:** <concise reusable answer>

**Type:** <CONCEPTUAL or HYBRID>
**Tags:** <tag1>, <tag2>, <tag3>
**Source:** cline conversation

---
```

Confirmation
- `Classification:` <CONCEPTUAL or HYBRID or IMPLEMENTATION>
- `Rewritten question:` <clean rewritten question or skipped>
- `Target file:` `docs/daily/YYYY-MM-DD_Knowledge_Base.md`
