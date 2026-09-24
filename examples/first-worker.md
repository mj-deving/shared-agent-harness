# First visible worker

Start with one read-only task. Use an existing scratch checkout you own; creating or selecting
that checkout is separate from terminal control. Install `cmux-orchestrate` and verify that your
orchestrator can read it in a fresh session.

Give the orchestrator this brief, replacing the directory:

```text
Use cmux-orchestrate. Create one uniquely named cmux workspace rooted at
<absolute scratch checkout>. Launch Claude Code using its normal permissions.
Verify the agent is ready before sending this task:

Read the README. Suggest one concrete clarification in at most five sentences.
Do not edit files, run project scripts, use network tools, or publish anything.

Read the completed response from that exact surface. Report the workspace identity,
provider readiness, worker result and whether the checkout remained unchanged.
Leave the idle workspace open so I can inspect it.
```

The orchestrator should inspect Git status before and after, including pre-existing changes.
A terminal opening is the first milestone, not the finish. If the provider asks for login or
workspace trust, resolve that prompt through normal controls before continuing.

To use Codex as the worker, replace the provider with Codex CLI. For writable tasks, first
allocate a dedicated worktree and specify the allowed files and tests. A separate agent session
is not itself filesystem isolation.

## From one worker to a DEMOS workflow

Start with a local fixture and a short behavior contract. Assign implementation to one worker,
then run code review and source-blind behavior validation with separate context. Let the
orchestrator reconcile both against the contract. Bind any later testnet or deployment effect
to a separate explicit task; do not copy another operator's accounts or node inventory.
