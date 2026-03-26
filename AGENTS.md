# Repo Knowledge Agent Guidance

Use the `repo-knowledge-capture` skill when a conversation contains reusable conceptual or teaching-oriented technical insight.

Trigger knowledge capture for:
- reusable explanations
- architecture reasoning
- tradeoff analysis
- framework or system design discussions
- conceptual comparisons that will be useful again

Do not trigger knowledge capture for:
- pure implementation work
- refactors
- debugging-only tasks
- tests
- shell tasks
- git operations
- dependency installation
- one-off fixes
- one-off file inspection

Do not capture explanations of existing repo code unless the explanation has clear reusable value beyond this repository.

When capture is appropriate, prefer deterministic file writing through the local writer script instead of ad hoc manual edits:

```bash
python skills/repo-knowledge-capture/scripts/kb_writer.py ...
```
