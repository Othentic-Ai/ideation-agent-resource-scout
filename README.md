# Ideation Agent: Resource Scout

Resource Scout & Technical Feasibility Evaluator for the Ideation Pipeline.

## Overview

This agent is part of the [Ideation multi-agent pipeline](https://github.com/Othentic-Ai/ideation-claude). It runs as Claude Code triggered via webhook.

**Role:** Finds datasets, APIs, tools and assesses technical complexity

**Output:** Available resources, technical feasibility assessment, build vs buy recommendations

## Architecture

```
┌─────────────────────────────┐
│    Ideation Orchestrator    │
│     (Cursor Slack App)      │
└──────────────┬──────────────┘
               │ repository_dispatch
               ▼
┌────────────────────────┐
│  Resource Scout Agent  │  ◄── This repo
│     (Claude Code)      │
└────────────┬───────────┘
               │
               ▼
┌─────────────────────────────┐
│            Mem0             │
│      (Shared Context)       │
└─────────────────────────────┘
```

## Repository Structure

```
ideation-agent-resource-scout/
├── CLAUDE.md        # Agent instructions (Claude Code reads this)
├── README.md        # This file
└── .github/
    └── workflows/
        └── run.yml  # Webhook trigger
```

## How It Works

1. **Triggered**: Orchestrator sends `repository_dispatch` webhook
2. **Execution**: GitHub Actions runs Claude Code CLI
3. **Instructions**: Claude Code reads `CLAUDE.md` for agent behavior
4. **Output**: Results written to Mem0 for next agent

## Trigger via Webhook

```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Othentic-Ai/ideation-agent-resource-scout/dispatches \
  -d '{"event_type": "run", "client_payload": {"session_id": "abc123", "problem": "Your problem"}}'
```

## Part of Ideation Pipeline

This agent is one of 9 specialized agents:

| Agent | Repository |
|-------|------------|
| Researcher | [ideation-agent-researcher](https://github.com/Othentic-Ai/ideation-agent-researcher) |
| Market Analyst | [ideation-agent-market-analyst](https://github.com/Othentic-Ai/ideation-agent-market-analyst) |
| Customer Discovery | [ideation-agent-customer-discovery](https://github.com/Othentic-Ai/ideation-agent-customer-discovery) |
| Scoring Evaluator | [ideation-agent-scoring-evaluator](https://github.com/Othentic-Ai/ideation-agent-scoring-evaluator) |
| Competitor Analyst | [ideation-agent-competitor-analyst](https://github.com/Othentic-Ai/ideation-agent-competitor-analyst) |
| Resource Scout | [ideation-agent-resource-scout](https://github.com/Othentic-Ai/ideation-agent-resource-scout) |
| Hypothesis Architect | [ideation-agent-hypothesis-architect](https://github.com/Othentic-Ai/ideation-agent-hypothesis-architect) |
| Pivot Advisor | [ideation-agent-pivot-advisor](https://github.com/Othentic-Ai/ideation-agent-pivot-advisor) |
| Report Generator | [ideation-agent-report-generator](https://github.com/Othentic-Ai/ideation-agent-report-generator) |

Orchestrated by: [ideation-claude](https://github.com/Othentic-Ai/ideation-claude)

## License

MIT
