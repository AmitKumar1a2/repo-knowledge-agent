# Repo Knowledge Agent (RKCA)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)](#)
[![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red.svg)](#)

Capture reusable technical learning from developer conversations directly inside the repository.

## What It Is

Repo Knowledge Agent is a local-file-based workflow for turning conceptual AI conversations into daily markdown knowledge files stored in the repo. It is built for practical engineering teams that want reusable technical learning, not full chat archives.

This repository already includes the Cline integration under `.clinerules/`. The Codex-facing files complement that setup with repo-native skill instructions, deterministic local writing, examples, and documentation.

## Why It Exists

Useful architectural reasoning, tradeoff analysis, and conceptual explanations often disappear into chat history. RKCA keeps the reusable learning and skips implementation noise so the repo becomes a durable knowledge surface instead of a temporary conversation log.

## Problem It Solves

- architecture reasoning gets lost after the session ends
- tradeoff discussions have to be repeated
- reusable conceptual explanations never make it into the repo
- implementation-heavy chat buries the few insights worth saving

## Use This Repo With Codex Or Cline

This repository is designed to work in both Codex and Cline.

- In Codex, the entry point is [`AGENTS.md`](./AGENTS.md), which points Codex to the local skill and writer script.
- In Cline, the entry point is the existing `.clinerules/` setup, which handles classification, logging rules, and the manual workflow.

Both paths write reusable knowledge into:

```text
docs/daily/YYYY-MM-DD_Knowledge_Base.md
```

## Architecture Overview

```text
Developer conversation
  -> classify task
  -> keep only conceptual or concept-heavy hybrid learning
  -> rewrite as reusable Q/A
  -> assign tags
  -> append to docs/daily/YYYY-MM-DD_Knowledge_Base.md
```

## Logging Rules

Log only when the conversation is:

- `CONCEPTUAL`
- `HYBRID` with substantial conceptual value

Skip logging for:

- direct code modifications
- debugging-only work
- refactors
- tests
- shell-only tasks
- git tasks
- dependency installation
- one-off fixes
- one-off repo inspection
- explanations of existing repo code unless they have broad reusable value

## 🔌 Works With

- Cline (rules + workflows)
- Codex (skills + `AGENTS.md`)
- Any LLM workflow that supports structured prompts

## Use Cases

- AI-first developers who learn through technical conversations
- Teams using Cline or Codex as part of day-to-day engineering work
- Learning-heavy workflows where architectural reasoning should stay with the repo
- RAG system builders comparing retrieval strategies and design tradeoffs
- Backend engineers documenting reusable architecture decisions

## How Codex Uses `AGENTS.md` And The Skill

Codex should read [`AGENTS.md`](./AGENTS.md) at the repo root and use it as the entry point for repo behavior.

When a conversation contains reusable conceptual or teaching-oriented technical insight, Codex should use:

```text
skills/repo-knowledge-capture/SKILL.md
```

The skill instructs Codex to:

1. classify the task as `CONCEPTUAL`, `IMPLEMENTATION`, or `HYBRID`
2. log only concept-worthy conversations
3. rewrite the user request as a reusable knowledge question
4. summarize the reusable answer
5. assign 2 to 5 tags
6. prefer deterministic writing through the local Python writer
7. skip duplicates by exact normalized question match within the same daily file

## How Cline Uses `.clinerules`

Cline already has repo-native integration in this repository. The main files are:

```text
.clinerules/repo-knowledge-capture.md
.clinerules/conceptual-only.md
.clinerules/workflows/capture-knowledge.md
```

The Cline rules tell the agent to:

1. classify each request as `CONCEPTUAL`, `IMPLEMENTATION`, or `HYBRID`
2. log only `CONCEPTUAL` requests and `HYBRID` requests with substantial conceptual value
3. skip implementation-only work such as code changes, refactors, shell tasks, and git tasks
4. rewrite the user request as a reusable knowledge question
5. summarize the reusable answer
6. assign tags
7. append the result to `docs/daily/YYYY-MM-DD_Knowledge_Base.md`
8. avoid duplicate questions in the same daily file

The manual workflow gives Cline an explicit capture path when you want to save the strongest reusable learning from the current context.

## Python Writer Script

Use the local writer script for deterministic file creation and duplicate prevention:

```bash
python skills/repo-knowledge-capture/scripts/kb_writer.py \
  --question "Why use MCP instead of relying only on raw prompts?" \
  --answer "MCP gives the model a structured interface to tools, context, and external systems, which improves reliability and reduces prompt sprawl." \
  --type CONCEPTUAL \
  --tags "mcp,prompting,tooling" \
  --date 2026-03-26
```

Behavior:

- writes to `docs/daily/YYYY-MM-DD_Knowledge_Base.md`
- creates `docs/daily/` if missing
- initializes a new daily file with `# Knowledge Base - YYYY-MM-DD`
- appends entries in the standard markdown format
- skips duplicates using exact normalized question matching inside the target daily file

## Example Output

```md
# Knowledge Base - 2026-03-26

## Q: What is the difference between MMR and plain similarity search in a RAG pipeline?
**A:** Plain similarity search returns the nearest matches by score, which can produce redundant chunks. MMR trades a small amount of raw similarity for diversity, making retrieved context more likely to cover distinct aspects of the query.

**Type:** CONCEPTUAL
**Tags:** rag, retrieval, mmr, similarity-search
**Source:** codex conversation

---
```

## Expected Behavior

```text
"Explain MMR vs similarity search in RAG" => logged
"Refactor this function" => skipped
"Why use MCP instead of raw prompts?" => logged
"Fix this failing unit test" => skipped
```

## 🏷️ Suggested GitHub Topics

- ai-agents
- developer-tools
- codex
- cline
- llm-workflows
- knowledge-management
- agentic-ai

## Repository Structure

```text
repo-knowledge-agent/
|-- .github/
|   |-- CONTRIBUTING.md
|   |-- ISSUE_TEMPLATE/
|   |   |-- bug_report.md
|   |   `-- feature_request.md
|   `-- workflows/
|       `-- placeholder.yml
|-- assets/
|   `-- demo/
|       |-- before-after.md
|       `-- demo-script.md
|-- AGENTS.md
|-- docs/
|   `-- daily/
|       `-- 2026-03-26_Knowledge_Base.md
|-- skills/
|   `-- repo-knowledge-capture/
|       |-- references/
|       |   `-- examples.md
|       |-- scripts/
|       |   `-- kb_writer.py
|       `-- SKILL.md
|-- .clinerules/
|   |-- conceptual-only.md
|   |-- repo-knowledge-capture.md
|   `-- workflows/
|       `-- capture-knowledge.md
|-- .gitignore
|-- LICENSE
`-- README.md
```

## Roadmap

- add a shared write path so Cline and Codex can optionally use the same script
- support merge-friendly duplicate handling for near-duplicates
- add summary generation across daily files
- add stronger examples for hybrid conceptual capture
