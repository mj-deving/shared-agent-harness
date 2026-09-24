# Twenty selected capabilities

The first nine are direct skills. The other eleven are loaded through two routers: 20 capabilities, 11 installed skill folders per harness. This is a curated selection, not a usage-frequency ranking.

## Shared foundation

| # | Skill | Why it is here | Dependencies / limits |
|---|---|---|---|
| 1 | [cmux-orchestrate](../skills/cmux-orchestrate/SKILL.md) | Visible cross-harness workers. | macOS cmux, installed/authenticated worker CLIs, authorized socket access. |
| 2 | [autoreview](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/autoreview) | Independent code review through supported agent CLIs. | Reviewer CLI and secret-scanner prerequisites. |
| 3 | [behavior-validator](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/behavior-validator) | Test observable behavior against a written contract. | Runnable target and suitable CLI/browser access; source-blind context. |
| 4 | [handoff](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/handoff) | Prepare a self-contained agent handoff. | Clipboard integration is optional; a handoff does not itself authorize action. |
| 5 | [session-viewer](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/session-viewer) | Inspect a session as searchable HTML. | Supported transcript format; review/redact before sharing. |
| 6 | [github-public-writing](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/github-public-writing) | Prepare clear, actionable public GitHub prose. | Public source context; publication needs explicit authority. |
| 7 | [govern-agent-context](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/govern-agent-context) | Keep startup context small and deeper docs discoverable. | Owner access to the relevant instruction/doc surfaces. |
| 8 | [govern-agent-stack](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/govern-agent-stack) | Decide what tooling belongs in a harness. | Use the consumer’s own policy and platform. |
| 9 | [govern-shared-skills](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/govern-shared-skills) | Maintain one owner and reproducible projections. | Use this starter or the consumer’s existing registry as owner. |

## LifeOS

Install the `lifeos` router or use `--profile curated`. Use it by name, for example “Use lifeos FirstPrinciples to challenge these assumptions.” The router reads one pinned body and translates runtime-specific behavior. Full LifeOS services are not installed.

| # | Workflow | Use |
|---|---|---|
| 10 | [FirstPrinciples](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/FirstPrinciples) | Challenge assumptions and rebuild from fundamental constraints. |
| 11 | [SystemsThinking](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/SystemsThinking) | Understand feedback loops and second-order effects. |
| 12 | [Science](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/Science) | Frame falsifiable hypotheses and experiments. |
| 13 | [Research](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/Research) | Synthesize evidence from sources; needs search/browser tools. |
| 14 | [Council](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/Council) | Compare perspectives through an explicit debate; independent agents need native dispatch. |
| 15 | [RedTeam](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/RedTeam) | Stress-test a proposal against concrete objections. |
| 16 | [ExtractWisdom](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/ExtractWisdom) | Extract useful ideas from accessible articles, talks or transcripts. |
| 17 | [ISA](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/ISA) | State the desired outcome with verifiable criteria; runtime synchronization is separate. |

## Agent Scripts

Install the `agent-scripts` router or use `--profile curated`. Each leaf retains its own CLI dependencies. The router excludes the vendor author’s personal accounts, hosts and authorization assumptions.

| # | Workflow | Use |
|---|---|---|
| 18 | [github-deep-review](https://github.com/steipete/agent-scripts/tree/c46ea65b6323e8a2b6f441f8b6449ae731bc8f81/skills/github-deep-review) | Trace a GitHub issue or PR through code and evidence; requires Git/gh. |
| 19 | [video-transcript-downloader](https://github.com/steipete/agent-scripts/tree/c46ea65b6323e8a2b6f441f8b6449ae731bc8f81/skills/video-transcript-downloader) | Download transcripts/media where permitted; requires the leaf’s media tooling. |
| 20 | [instruments-profiling](https://github.com/steipete/agent-scripts/tree/c46ea65b6323e8a2b6f441f8b6449ae731bc8f81/skills/instruments-profiling) | Measure macOS performance with Instruments; requires Xcode tools. |

## Why not everything?

Private skill suites, credential adapters, account connectors, personal memory, host inventories and provider-managed plugins are outside this starter. Beads and the full LifeOS Algorithm remain optional project/runtime choices; they are not silently installed or replaced. Add capabilities when someone in the working group has a concrete use and can verify them.
