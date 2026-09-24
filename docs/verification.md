# Verification

Initial v0.1.0 candidate checked on macOS, 2026-09-24.

## Observed

- 14 isolated installer tests pass, including dry-run, idempotence, collisions, modified links,
  uninstall preservation, source reuse, dirty/wrong pins, owner-wide updates and error rollback.
- The curated profile fetched the three exact public source commits and created 22 links in a
  temporary home: the same 11 skill folders projected into Claude and Codex.
- A second curated check reported zero downloads and zero link changes.
- A fresh local Codex prompt diagnostic discovered the CMUX skill and both vendor routers
  from the isolated project loader. Existing user visibility settings hid some optional skills;
  they were preserved. This is not proof of complete fresh discovery in both personal loaders.
- All 11 routed leaf entrypoints resolved to existing files at their declared source pins.
- cmux 0.64.25 completed a live isolated shell-control test: unique workspace creation, UUID
  resolution, explicit send/Enter, executed marker readback and exact owned-workspace cleanup.
- A background workspace initially had no initialized readable terminal. The documented visible
  workflow now focuses its newly owned workspace and allows bounded waits for tree updates.
- An independent review identified partial source-update drift and a missing LifeOS documentation
  path mapping. Both were corrected; the update regression is covered by a test.

## Scope of proof

The cmux test ran a shell command, not a paid provider task. It establishes terminal control,
not Claude/Codex task quality. The installer tests establish ownership and file behavior,
not runtime availability of every optional tool. All 20 workflows have not been run end to end.
A source-blind behavior-validation campaign has not been performed for the entire catalog.

After installing, open fresh sessions in both harnesses. Confirm the installed names are
visible, ask each to read the actual skill, and use the first-worker example before assigning
writable work. Verify the effective model and permissions through the provider's own session.

No real user loader, existing agent session, account, permission policy, or production system
was changed for the installer tests. Temporary cmux workspaces were closed by exact identity.

## v0.2.0 expanded selection

- The catalog now covers 40 capabilities: 26 through the extended installer and 14 optional
  native/vendor workflows. The latter are provenance entries, not installed-state claims.
- All 14 installer tests still pass. An isolated extended installation reused three verified
  source checkouts, downloaded the exact Graph Climbing and Humanizer pins and created 26 links.
  Its next check reported zero downloads and zero link changes.
- All 15 routed LifeOS/agent-scripts entrypoints resolve. The four added LifeOS skills are BPE,
  Evals, IterativeDepth and BeCreative.
- The pinned Evals deterministic assertion self-test passed 16/16 cases under Bun. No model
  inference, model judge or multi-turn agent evaluation was run; those require their own setup.
- Waza is documented as a standalone official plugin. GStack, Impeccable and Watch keep their
  owner installers. No native suite, provider account or real user skill loader was changed.

This extends the installation and source-resolution proof. It does not establish full execution
of all 40 workflows or runtime discovery in every harness.
