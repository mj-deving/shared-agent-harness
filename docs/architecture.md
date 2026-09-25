# Architecture: the original system and this starter

The shared system centralizes ownership and routing. It does not require every skill to live
in the same repository, or pretend Claude and Codex have identical runtimes.

| Layer | Original architecture | Minimum starter |
|---|---|---|
| Canonical owners | Shared skills, LifeOS, vendor scripts, project skills, native plugins | Five pinned public sources plus this repo's adapter owner; four optional native/vendor suites |
| Registry | Source pins, admissions, target harnesses, adapters, conflicts | `sources.json`: owners, immutable pins, selected skills, profiles and routed catalogs |
| Shared projections | Individual symlinks into Claude/Codex loaders | Same pattern; preview/apply/check/uninstall with an ownership receipt |
| Vendor routing | Compact routers with lazy loading and generated discovery metadata | Two compact routers name 15 additional vendor leaves; CMUX resolves through its own adapter |
| LifeOS | Claude-native deployment; Codex router and Algorithm/ISA adapters | Both harnesses use a small explicit translation over pinned source workflows |
| CMUX | LifeOS CMUX skill plus a runtime overlay | Pinned, unchanged LifeOS CMUX skill, workflows and `cmux.ts`; portable `cmux-orchestrate` adapter resolves them |
| Shared instructions | Small startup routes; load detailed doctrine on demand | Optional project routing snippet, merged by the project owner |
| Durable work | Project specification, existing task ledger, Git/tests as evidence | Reuse those existing project surfaces; no second task system |
| Lifecycle integration | Claude hooks and a Codex adapter into installed LifeOS owners | Not installed; requires the full runtime and its own lifecycle owner |
| Plugins and private tools | Remain with their native/private owners | Not copied or reconfigured |

```text
sources.json ── install.py ── personal loader symlinks
     │                            ├── Claude Code
     │                            └── Codex
     ├── shared skills ───────────────── direct bodies
     ├── LifeOS source ── lifeos router ── selected body + harness translation
     └── vendor scripts ─ agent-scripts router ─ selected body + owner checks

cmux-orchestrate ── pinned LifeOS/CMUX ── cmux.ts ── visible agent workers
```

## What is intentionally the same

Each logical skill has one canonical owner. Upstream bodies remain unchanged. Compatible
skills are linked directly; incompatible runtime assumptions are handled in small adapters.
Descriptions expose routing without preloading all bodies. Installation, discovery, execution
and completion are different checks. The orchestrator owns integration and evidence.

A source may be downloaded once or explicitly reused from an existing clean, pinned checkout.
The receipt records reused source bindings. Two harness links point to the same canonical folder.
When a manifest pin changes, all installed direct projections for that source must be included
in the update; the installer refuses a selection that would leave an older projection behind.

## Deliberate differences

This is a functional starter for shared skills and terminal orchestration, not a backup or a
complete replica of the author's machine. The original registry is larger, uses Bun, and also
owns generated indexes and native runtime integration. This installer uses Python's standard
library and two bounded catalog routers; there is no need to install that infrastructure to
share a compact core.

Codex's documented personal skill directory is `.agents/skills`; older installations also use
`.codex/skills`. This starter defaults to the current documented location, supports explicit
loader paths and refuses detected legacy duplicates. Claude uses `.claude/skills`.

The minimal CMUX profile fetches the same pinned LifeOS checkout used by the larger router.
`resolve.py lifeos CMUX` returns the original skill and script paths from that checkout,
including a reused clean source binding. The script's relative Pulse import stays intact.
Its personal fleet and voice modes need additional LifeOS configuration or services. The
adapter gives both harnesses the resolved script path and keeps the direct CLI fallback.
At this pin, `boot-team` lays out shells; a provider must be launched in each selected pane.
`race` defaults to a readiness print and needs an explicit command to race real agents.

The LifeOS router translates notifications and tool mechanics for both harnesses while keeping
the workflow source pinned. It does not install voice, Pulse, memory, personal identity, hooks,
private overlays or the persistent Algorithm execution loop. A workflow requiring those
services reports the missing dependency. The ISA leaf can read its pinned format documents;
that is different from running the full LifeOS ISA lifecycle.

## If you already run LifeOS or another registry

Keep that owner in charge. Do not install a second LifeOS runtime or replace its native skills.
Select only missing starter skills with `--skills`, or register the portable CMUX adapter in
your existing registry. Reuse the full runtime's documented Claude installation and its existing
Codex translation when available. Do not copy the author's private hooks or configuration.

A later full-runtime package would need its own declared install/update/rollback contract and
fresh-session proof. It should delegate to canonical LifeOS lifecycle code rather than reimplement
its memory, task or dashboard schemas in this starter.

## Extending the starter

For a shared skill, add one owner/path admission and a focused test. For a vendor leaf, extend
its router description and catalog together so the new intent is discoverable. For a new harness,
verify its actual loader and runtime semantics before adding a target. Plugin-managed skills
stay with the plugin manager. Account/host names and credentials belong to the consumer's
configuration, never to a shared skill body.

## Broader selection

The 40-capability catalog separates 26 installer-managed capabilities from 14 selected workflows
managed by four native/vendor suites. `sources.json` records the latter under `external_suites`,
including the reviewed public revision and setup guide. These entries are provenance references,
not installed-state receipts. `--check` does not audit those external installations.

This mirrors the original ownership distinction: compatible skills share a body; Waza can remain
plugin-owned; GStack and Impeccable retain their generators and runtime assets; Watch retains its
media dependencies. The author's private cross-harness overlays are not exported. Users keep
existing suite owners or opt into their official setup, without a second competing projection.
