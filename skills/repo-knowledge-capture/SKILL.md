---
name: repo-knowledge-capture
description: Capture conceptual or teaching-oriented developer conversations into daily markdown knowledge-base entries. Use for reusable explanations, architecture reasoning, tradeoffs, framework design, and learning-oriented technical discussions.
---

# Repo Knowledge Capture

## When To Use This Skill

Use this skill when the conversation contains reusable technical learning, such as:
- explanations of concepts or patterns
- architecture reasoning
- design tradeoffs
- framework or system design guidance
- teaching-oriented comparisons that will help again later

## When Not To Use This Skill

Do not use this skill for:
- direct code modifications
- debugging-only work
- refactors
- tests
- shell-only tasks
- git tasks
- dependency installation
- one-off repo inspection
- explaining existing repo code unless it has broad reusable value

## Classification

Silently classify each task as exactly one of:
- `CONCEPTUAL`
- `IMPLEMENTATION`
- `HYBRID`

Log only when:
- classification is `CONCEPTUAL`, or
- classification is `HYBRID` with substantial conceptual value

Do not log `IMPLEMENTATION` tasks.

## Output Destination

Write entries to:

```text
docs/daily/YYYY-MM-DD_Knowledge_Base.md
```

If the daily file does not exist, create it with:

```md
# Knowledge Base - YYYY-MM-DD
```

Use this exact entry format:

```md
## Q: <clear rewritten question>
**A:** <concise reusable answer>

**Type:** <CONCEPTUAL or HYBRID>
**Tags:** <tag1>, <tag2>, <tag3>
**Source:** codex conversation

---
```

## Rewriting Rules

- Rewrite the request as a clean, reusable question.
- Remove repo-specific phrasing unless it is essential to the concept.
- Prefer general technical wording over task-specific wording.
- Keep the answer concise, accurate, and reusable.
- Do not paste raw conversation transcripts.

## Tagging Rules

- Assign 2 to 5 tags.
- Use short, practical, developer-oriented tags.
- Prefer concept names, architecture terms, or technology areas.
- Avoid duplicate or near-duplicate tags in the same entry.

## Duplicate Prevention

- Before writing, check the target daily file for the same question.
- Treat duplicate detection as an exact match on a normalized question string.
- If the question already exists, skip writing a second copy.

## Operational Sequence

1. Classify the task as `CONCEPTUAL`, `IMPLEMENTATION`, or `HYBRID`.
2. Stop if the task is `IMPLEMENTATION`.
3. If the task is `HYBRID`, continue only when the conceptual value is substantial.
4. Rewrite the user request as a reusable knowledge question.
5. Summarize the reusable answer.
6. Assign 2 to 5 tags.
7. Write the entry to today's daily knowledge-base file.
8. Skip the write if the normalized question already exists in that file.

## Preferred Write Path

Prefer the local Python writer script over ad hoc manual edits:

```bash
python skills/repo-knowledge-capture/scripts/kb_writer.py \
  --question "..." \
  --answer "..." \
  --type CONCEPTUAL \
  --tags "tag1,tag2,tag3"
```
