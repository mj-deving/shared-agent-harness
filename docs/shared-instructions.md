# Optional project routing

Merge the following into a shared, project-owned document (for example `AGENT_WORKFLOW.md`).
Add `Read AGENT_WORKFLOW.md before delegating work.` to both existing `AGENTS.md` and `CLAUDE.md`.
Review the resulting instructions against the project's own rules; the installer does not edit them.

```text
Use native subagents for bounded work inside the current harness when permitted.
Use cmux-orchestrate for visible independent sessions or cross-harness delegation.
Read the selected skill before operating its tools.

Give each worker a goal, exact workspace, permitted changes, prohibited effects,
completion criteria and expected evidence. Parallel writers use isolated worktrees.
One controller owns each interactive session. The orchestrator verifies results
and integrates changes; a worker report alone does not establish completion.

Keep each skill's source in one owner repository. Harness loader folders contain
managed links or thin adapters. Do not edit a projection as if it were the source.

Use autoreview when an independent code review is requested; use behavior-validator
for observable behavior against a prewritten contract. Keep the latter source-blind.
Use the project's existing task tracker and specification for durable ownership and
completion. Do not create a second task ledger just because another agent joined.

No worker may expand the user's authority. External sends, publication, live
transactions and deployments require the project's explicit authorization.
```

For DACS/DEMOS tasks, add the specific repository, standard/spec revision and network to the
worker brief. Do not assume a testnet permission also authorizes mainnet, or that reviewing a PR
authorizes posting a review. This starter establishes no normative protocol interpretation.
