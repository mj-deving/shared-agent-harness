# Forty selected capabilities

A selection across the full working stack, not just LifeOS and not a usage-frequency ranking.

| Group | Capabilities | Install mode |
|---|---:|---|
| Shared/CMUX + LifeOS + agent-scripts | 24 | `--profile curated` |
| Graph Climbing + Humanizer | 2 | Added by `--profile extended` |
| Waza | 8 | Native/vendor installer |
| GStack | 4 | Vendor build and harness projections |
| Impeccable + Watch | 2 | Native/vendor installer |
| **Total** | **40** | **26 through this installer; 14 opt-in through their owners** |

The LifeOS selection includes CMUX plus BPE, Evals and ten thinking/research/specification workflows. CMUX is counted once in the 40, under the shared foundation. The extended profile exposes 26 capabilities through 13 skill folders per harness. Optional suites may install more modules than our selected shortlist. All sources retain their ownership and license.

## Shared foundation

| # | Skill | Why it is here | Dependencies / limits |
|---|---|---|---|
| 1 | [cmux-orchestrate](../skills/cmux-orchestrate/SKILL.md) → [LifeOS CMUX](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/CMUX) | Visible cross-harness workers using the actual pinned skill, workflows and `cmux.ts`. | Bun, macOS cmux, authenticated worker CLIs and socket access; optional voice/fleet modes need LifeOS setup. |
| 2 | [autoreview](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/autoreview) | Independent code review through supported agent CLIs. | Reviewer CLI and secret-scanner prerequisites. |
| 3 | [behavior-validator](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/behavior-validator) | Test observable behavior against a written contract. | Runnable target and suitable CLI/browser access; source-blind context. |
| 4 | [handoff](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/handoff) | Prepare a self-contained agent handoff. | Clipboard integration is optional; a handoff does not itself authorize action. |
| 5 | [session-viewer](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/session-viewer) | Inspect a session as searchable HTML. | Supported transcript format; review/redact before sharing. |
| 6 | [github-public-writing](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/github-public-writing) | Prepare clear, actionable public GitHub prose. | Public source context; publication needs explicit authority. |
| 7 | [govern-agent-context](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/govern-agent-context) | Keep startup context small and deeper docs discoverable. | Owner access to the relevant instruction/doc surfaces. |
| 8 | [govern-agent-stack](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/govern-agent-stack) | Decide what tooling belongs in a harness. | Use the consumer’s own policy and platform. |
| 9 | [govern-shared-skills](https://github.com/mj-deving/agent-skills/tree/7d4d219626c46d3c1d664a5a3e2206ed2cfd623e/skills/govern-shared-skills) | Maintain one owner and reproducible projections. | Use this starter or the consumer’s existing registry as owner. |

## LifeOS

Install the `lifeos` router or use `--profile curated`. Use it by name, for example “Use lifeos FirstPrinciples to challenge these assumptions.” The router reads one pinned body and translates runtime-specific behavior. The CMUX adapter uses the same LifeOS checkout for the original CMUX package. Full LifeOS services are not installed.

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
| 18 | [BitterPillEngineering / BPE](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/BitterPillEngineering) | Audit over-prompting and redundant rules; preserve safety and verified tool contracts. |
| 19 | [Evals](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/Evals) | Design assertion-first suites and judge criteria; execution needs Bun, the appropriate inference/runtime setup and an authorized trial budget. |
| 20 | [IterativeDepth](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/IterativeDepth) | Explore a question through several lenses to uncover missing requirements. |
| 21 | [BeCreative](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/BeCreative) | Generate diverse ideas, alternatives and test examples. |

## Agent Scripts

Install the `agent-scripts` router or use `--profile curated`. Each leaf retains its own CLI dependencies. The router excludes the vendor author’s personal accounts, hosts and authorization assumptions.

| # | Workflow | Use |
|---|---|---|
| 22 | [github-deep-review](https://github.com/steipete/agent-scripts/tree/c46ea65b6323e8a2b6f441f8b6449ae731bc8f81/skills/github-deep-review) | Trace a GitHub issue or PR through code and evidence; requires Git/gh. |
| 23 | [video-transcript-downloader](https://github.com/steipete/agent-scripts/tree/c46ea65b6323e8a2b6f441f8b6449ae731bc8f81/skills/video-transcript-downloader) | Download transcripts/media where permitted; requires the leaf’s media tooling. |
| 24 | [instruments-profiling](https://github.com/steipete/agent-scripts/tree/c46ea65b6323e8a2b6f441f8b6449ae731bc8f81/skills/instruments-profiling) | Measure macOS performance with Instruments; requires Xcode tools. |

## More shared skills

| # | Skill | Why it is here | Dependencies / limits |
|---|---|---|---|
| 25 | [Graph Climbing](https://github.com/mj-deving/graph-climbing/tree/192d7785fc969c1f69634927a23bd2433715b23b/adapters/graph-climbing-skill) | Coordinate durable work, claims, evidence and safe parallelism. | Reuses the project's spec/ledger; optional TypeScript checkers require their documented runtime. |
| 26 | [Humanizer](https://github.com/mj-deving/humanizer/tree/d4fed7bd33a1bb59d2ca4f3a27816ec17b7d4ee6) | Edit prose for natural language while preserving facts. | Shared source; no API or service required for the instruction workflow. |

## Waza: focused daily workflows

Keep Waza as its own official plugin. Use the [Waza owner setup](optional-suites.md#waza). These are alternatives or complements to the existing workflows, not instructions to run every review tool on every task.

| # | Skill | Use |
|---|---|---|
| 27 | think | Turn a rough idea into a concrete plan. |
| 28 | hunt | Find a bug's root cause before changing code. |
| 29 | check | Review code and release readiness. |
| 30 | health | Audit agent instructions, hooks and verifier coverage. |
| 31 | learn | Research and synthesize unfamiliar material. |
| 32 | read | Read URLs and PDFs into usable source material. |
| 33 | write | Draft, rewrite and polish prose. |
| 34 | ui | Build and refine interfaces. |

Source: [Waza at the reviewed revision](https://github.com/tw93/Waza/tree/663f27eb136118c0a3aa78b5ce9e712b7aee7f0a/skills).

## GStack: deeper product and engineering workflows

Use the [GStack owner setup](optional-suites.md#gstack). Its runtime and generated harness outputs are part of the capability; copying a leaf's Markdown alone is insufficient.

| # | Module | Use |
|---|---|---|
| 35 | plan-ceo-review | Challenge product scope and value. |
| 36 | plan-eng-review | Review architecture and implementation plans. |
| 37 | qa | Exercise a running site through the browser. |
| 38 | ship | Prepare and execute an authorized shipping workflow. |

Source: [GStack at the reviewed revision](https://github.com/garrytan/gstack/tree/0d1bd5616c0ef096bb7ccee336f63c60ee408618).

## Design and video

| # | Skill | Use | Setup |
|---|---|---|---|
| 39 | Impeccable | Design direction, critique, accessibility and interface polish. | [Vendor-generated harness builds](optional-suites.md#impeccable) |
| 40 | Watch | Inspect video frames and transcripts with timestamps. | [Upstream video skill](optional-suites.md#watch); media tools and optional transcription credentials are separate. |

## Pick by job

Start with CMUX, handoff, autoreview and behavior-validator. Add Graph Climbing for durable multi-session work. Choose Waza for focused planning/debugging/writing; use GStack when its deeper product/browser/release workflow fits. Use Impeccable for interface design and Watch for recordings. These overlap intentionally; choose one primary workflow for a task instead of stacking all of them.

## Why not everything?

Private skills, credential brokers, personal memory and machine inventories are not portable defaults. Provider-managed browser/document/security plugins remain outside this release because their availability and permissions belong to each user's installation. The shortlist can grow from working-group usage; a larger catalog is not automatically a better starting configuration.
