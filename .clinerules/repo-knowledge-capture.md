# Repo Knowledge Capture

Purpose: capture only reusable conceptual learning from Cline conversations into daily markdown files stored in this repository.

Classification
- Classify every request as exactly one of:
- `CONCEPTUAL`: primarily asks for explanation, comparison, tradeoffs, principles, architecture, or reusable teaching.
- `IMPLEMENTATION`: primarily asks for code changes, bug fixes, refactors, shell actions, git actions, or repo-specific execution.
- `HYBRID`: contains both implementation work and meaningful conceptual explanation.

Logging Rules
- Log when classification is `CONCEPTUAL`.
- Log when classification is `HYBRID` and the conversation contains substantial conceptual value that is reusable beyond the immediate task.
- Do not log:
- direct code modifications
- bugfix-only work
- refactors
- shell-only tasks
- git tasks
- explanations of existing repo code unless the explanation is broadly reusable outside this repository

Target File
- Append entries to `docs/daily/YYYY-MM-DD_Knowledge_Base.md`.
- Replace `YYYY-MM-DD` with the current local date for the session.
- If the daily file does not exist, create it with this first line:

```md
# Knowledge Base - YYYY-MM-DD
```

Entry Format

```md
## Q: <clear rewritten question>
**A:** <concise reusable answer>

**Type:** <CONCEPTUAL or HYBRID>
**Tags:** <tag1>, <tag2>, <tag3>
**Source:** cline conversation

---
```

Required Agent Steps
1. Classify the request as `CONCEPTUAL`, `IMPLEMENTATION`, or `HYBRID`.
2. If logging is allowed, rewrite the user request as a reusable knowledge question.
3. Summarize the reusable answer in a concise, teaching-oriented form.
4. Assign 2-5 practical tags.
5. Append the entry to today's file.

Duplicate Prevention
- Before appending, check whether the same rewritten question already exists in the target daily file.
- Treat duplicate detection as an exact match on a normalized question string.
- If a duplicate exists, skip appending instead of writing a second copy.

Writing Guidance
- Keep entries concise and reusable.
- Prefer general principles over repo-specific details.
- Do not include raw transcripts.
- Do not capture implementation noise when the reusable learning is absent.
