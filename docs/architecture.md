# Architecture: the original system and this starter

The shared system centralizes ownership and routing. It does not require every skill to live
in the same repository, or pretend Claude and Codex have identical runtimes.

| Layer | Original architecture | Minimum starter |
|---|---|---|
| Canonical owners | Shared skills, LifeOS, vendor scripts, project skills, native plugins | Three pinned public sources plus this repo's adapter owner |
| Registry | Source pins, admissions, target harnesses, adapters, conflicts | `sources.json`: owners, immutable pins, selected skills, profiles and routed catalogs |
| Shared projections | Individual symlinks into Claude/Codex loaders | Same pattern; preview/apply/check/uninstall with an ownership receipt |
| Vendor routing | Compact routers with lazy loading and generated discovery metadata | Two compact routers whose descriptions name all 11 admitted vendor leaves |
| LifeOS | Claude-native deployment; Codex router and Algorithm/ISA adapters | Both harnesses use a small explicit translation over pinned source workflows |
| CMUX | LifeOS CMUX skill plus a runtime overlay | Standalone `cmux-orchestrate` adapter preserving the control/verification rules |
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

cmux-orchestrate ── local cmux CLI ── explicitly scoped terminal workers
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
share 20 capabilities.

Codex's documented personal skill directory is `.agents/skills`; older installations also use
`.codex/skills`. This starter defaults to the current documented location, supports explicit
loader paths and refuses detected legacy duplicates. Claude uses `.claude/skills`.

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
