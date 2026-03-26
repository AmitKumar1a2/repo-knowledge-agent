# Repo Knowledge Capture Agent

Repo Knowledge Capture Agent is a lightweight, Cline-first pattern for saving reusable conceptual learning from AI conversations into daily markdown files inside the repository.

It exists to preserve teaching-oriented knowledge without polluting the repo with implementation noise. The goal is to keep the knowledge base useful, readable, and portable across projects.

## What It Captures

The system captures only conceptual or concept-heavy hybrid conversations, such as explanations, tradeoffs, architecture guidance, and broadly reusable teaching.

It does not capture implementation-only activity such as code edits, refactors, bugfixes, shell work, git work, or repo-specific explanations that are not reusable outside the immediate task.

## File Structure

```text
.clinerules/
  conceptual-only.md
  repo-knowledge-capture.md
  workflows/
    capture-knowledge.md
docs/
  daily/
    YYYY-MM-DD_Knowledge_Base.md
scripts/
  kb_writer.py
```

## How Cline Uses the Rules

The persistent rule file in `.clinerules/repo-knowledge-capture.md` tells Cline to:
- classify each request as `CONCEPTUAL`, `IMPLEMENTATION`, or `HYBRID`
- log only `CONCEPTUAL` requests and `HYBRID` requests with substantial conceptual value
- rewrite the original request into a reusable question
- write a concise reusable answer
- assign 2-5 tags
- append the result to `docs/daily/YYYY-MM-DD_Knowledge_Base.md`
- skip duplicate questions in the same daily file

The scope guard in `.clinerules/conceptual-only.md` reinforces that implementation-only work should not be logged.

## Manual Workflow

The manual workflow lives at `.clinerules/workflows/capture-knowledge.md`.

Invoke it when you want to explicitly capture the strongest reusable learning from the current conversation. The workflow reviews context, classifies the request, rewrites the question, writes a concise answer, assigns tags, and appends to today's knowledge-base file. If a near-duplicate exists, it should merge rather than add redundant content.

The workflow also includes a short confirmation block with:
- classification
- rewritten question
- target file path

## Python Writer Script

Use the local writer when you want deterministic file creation and duplicate prevention:

```bash
python scripts/kb_writer.py \
  --question "When should you use MMR instead of plain similarity search in a RAG pipeline?" \
  --answer "Use similarity search for the closest matches only, and MMR when you also want diverse coverage across retrieved chunks." \
  --type CONCEPTUAL \
  --tags "rag,retrieval,mmr"
```

Optional date override:

```bash
python scripts/kb_writer.py \
  --question "Why use MCP instead of relying only on raw prompts?" \
  --answer "MCP provides structured access to tools and context, which improves reliability and reduces prompt sprawl." \
  --type CONCEPTUAL \
  --tags "mcp,prompting,tooling" \
  --date 2026-03-26
```

Behavior:
- creates `docs/daily/` if missing
- initializes a new daily file with `# Knowledge Base - YYYY-MM-DD`
- appends entries in the standard markdown format
- skips duplicates based on exact normalized question match within the target daily file

## Expected Behavior Examples

- `Explain MMR vs similarity search in RAG` => log
- `Refactor this function` => skip
- `Why use MCP instead of raw prompts?` => log
- `Fix this failing unit test` => skip
