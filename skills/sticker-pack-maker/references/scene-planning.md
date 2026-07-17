# Scene planning

## Diversity matrix

Distribute scenes across different communication functions:

| Function | Examples |
| --- | --- |
| Greeting | Hi, welcome, good morning |
| Acknowledgement | Got it, understood, received |
| Progress | Checking, processing, generating |
| Success | Done, approved, shipped |
| Failure | Sorry, failed, retrying |
| Waiting | One moment, queued, pending |
| Decision | Let me think, reviewing, voting |
| Risk | Be careful, audit needed, DYOR |
| Motivation | Keep going, great work, bullish |
| Collaboration | Let's build, community, human + AI |

Avoid creating multiple scenes that differ only in bubble text. Give each scene a unique silhouette, prop, and emotion.

## Manifest schema

Planning manifests may contain rich fields:

```json
{
  "pack": "ai",
  "scenes": [
    {
      "index": 1,
      "text": "正在思考",
      "action": "hand on chin with floating thought nodes",
      "emotion": "focused",
      "filename": "01_正在思考.png"
    }
  ]
}
```

For post-processing random generator filenames, add a `source` field to every scene:

```json
{
  "source": "exec-1234.png",
  "filename": "01_正在思考.png"
}
```

## Domain heuristics

- Workplace: emphasize status, ownership, handoff, meetings, deadlines, and support.
- Web3: include wallets, chains, gas, bridges, minting, governance, audits, and market emotions.
- AI: include prompting, retrieval, training, inference, agents, tools, hallucination checks, and human review.
- Community: include welcome, moderation, announcements, voting, events, and collaboration.

Use technical jargon only when the audience already uses it. Keep bubble text readable at chat-thumbnail size.
