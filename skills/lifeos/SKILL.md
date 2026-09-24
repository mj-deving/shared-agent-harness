---
name: lifeos
description: "Route eight shared LifeOS workflows: FirstPrinciples for assumptions, SystemsThinking for feedback loops, Science for experiments, Research for source synthesis, Council for debate, RedTeam for adversarial critique, ExtractWisdom for takeaways, and ISA for verifiable desired outcomes. Not the full LifeOS runtime installer."
---

# Shared LifeOS router

The LifeOS source owns workflow semantics. This starter owns only source resolution and harness
translation. Both Claude and Codex use the same pinned bodies, loaded one at a time.

1. Resolve this skill's symlink to its real source directory. The starter root is two parents
   above that directory. Read its `sources.json` for the exact admitted catalog.
2. Choose one exact leaf from the description. Announce it. Run
   `python3 <starter-root>/resolve.py lifeos <ExactName>` through properly quoted arguments.
   This read-only helper verifies the source revision and cleanliness and returns the canonical
   path. On drift or a missing source, stop and report the dependency; do not fetch or alter it.
3. Read that complete `SKILL.md`. Resolve relative workflows/assets from its directory.
4. Apply the following starter translation to both harnesses. It overrides runtime-specific
   instructions in the vendor body; the upstream files stay unchanged.
5. Read only the resources needed for this task, perform the workflow, and verify its result.

## Starter translation

- Replace voice/Pulse calls with a concise text progress message. Do not call localhost services,
  write LifeOS memory/logs, start hooks, or import another operator's persona or USER directory.
- Interpret vendor `~/.claude/skills/<Name>` references as paths under the resolved source's
  `LifeOS/install/skills`. Map read-only `~/.claude/LIFEOS/DOCUMENTATION/<path>` or
  `LIFEOS/DOCUMENTATION/<path>` references to `<source_root>/LifeOS/install/LIFEOS/DOCUMENTATION/<path>`.
  Likewise resolve read-only ALGORITHM references under that same pinned `LifeOS/install/LIFEOS`
  tree. Preserve the source's actual path casing; do not read another installed version accidentally.
  Resolve only existing supporting resources. Do not create a fake
  `~/.claude/LIFEOS` runtime. A helper requiring deployed runtime state needs a separately
  installed and authorized LifeOS runtime; otherwise report the blocked step.
- Translate tool names to available native tools without widening permissions. Use the current
  harness's native agents for permitted delegation, or `cmux-orchestrate` for visible cross-harness
  workers. Never pretend unavailable agents/tools executed. Preserve explicit model choices.
- Nested skill calls can use an already-installed native owner or this admitted catalog.
  Missing skills require an explicit dependency decision; do not silently install the full suite.
- For Research, use available search/browser tools and primary sources. For ExtractWisdom,
  require accessible source content; video extraction tools are separate dependencies.
- For ISA, retain stable criteria and evidence in the owning project's agreed document. This
  starter does not install the Algorithm loop, Pulse synchronization or an execution ledger.
  Use the project's existing task system. Do not introduce mandatory logging paths.
- For Council/RedTeam, distinguish real independent workers from a single model considering
  several perspectives. Report unavailable concurrency; do not claim independent consensus.

## Existing full LifeOS installations

If LifeOS already owns a selected skill natively, use that owner rather than adding a competing
workflow. Install only the starter pieces you lack. The curated starter source is an immutable
public checkout; it is not a deployed LifeOS runtime. The full architecture and migration choices
are described in the starter's `docs/architecture.md`.
