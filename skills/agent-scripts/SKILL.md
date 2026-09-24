---
name: agent-scripts
description: "Route selected agent-scripts workflows: github-deep-review for code-aware GitHub investigation, video-transcript-downloader for transcripts and media extraction, instruments-profiling for macOS performance traces. Not a blanket install of the vendor catalog."
---

# Agent Scripts router

Keep vendor bodies with their pinned source owner. Read one leaf when needed.

1. Resolve this skill's symlink. The starter root is two parents above its real directory.
2. Run `python3 <starter-root>/resolve.py agent-scripts <exact-leaf-name>`, with properly quoted
   arguments. The read-only helper checks the manifest pin and source cleanliness.
3. Read the canonical leaf completely and resolve its relative resources there.
4. Check tool prerequisites before execution. Use the current user's authorization and
   project rules; vendor names, accounts, hosts and permissions describe their author, not you.
5. Native, plugin or project owners take precedence for an already-installed same capability.

## Translation and dependencies

- `github-deep-review`: requires Git, authenticated `gh` and the target repository. Translate
  vendor checkout paths to the resolved source. Skip author-specific privilege/identity
  exceptions and automatic contributor-note persistence. The optional author-context extension
  is not admitted here; a review can proceed without it, saying that it was omitted. No posting,
  merging or pushing unless the user authorized that action.
- `video-transcript-downloader`: check the selected leaf's downloader, ffmpeg, Node/runtime and
  authentication requirements. Keep recordings/cookies out of shared output. Missing tools are
  dependencies, not permission to install or extract credentials.
- `instruments-profiling`: requires macOS and the Xcode/Instruments tools named by the leaf.
  Bind the actual application/process before tracing; do not adopt a vendor app path or host.

Do not alter upstream files. Report the selected leaf, source pin, translation and actual proof.
