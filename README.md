# Shared Agent Harness

Use Codex to delegate to Claude Code, Claude to delegate to Codex, or either to steer another
terminal agent through cmux. Keep each shared skill in one canonical place and symlink it into
the harnesses you use.

A small, opt-in starter for DACS working-group members and DEMOS contributors. This is a
community toolkit, not an official DACS or DEMOS component. Take just the parts you want.

```text
                         cmux terminal sessions
Your orchestrator ──────┬── Claude Code worker
                        └── Codex CLI worker

One canonical skill folder ──┬── Claude's personal skill link
                             └── Codex's personal skill link
```

## Start with CMUX

You need Python 3.10+, Git, [cmux for macOS](https://cmux.com/docs/getting-started),
and whichever agent CLIs you want to run, already authenticated. The installer needs no
Python packages. It installs skill links, not cmux, agent CLIs, accounts, hooks, or services.
Agents use their own authentication and billing; this does not promise free or unlimited use.

```sh
git clone https://github.com/mj-deving/shared-agent-harness.git
cd shared-agent-harness
python3 install.py                     # preview; no writes or downloads
python3 install.py --apply             # CMUX skill, both harnesses
python3 install.py --check             # exit 0 when selected files/links match
```

Start a fresh Claude Code or Codex session and ask it to locate `cmux-orchestrate`, read the
skill, and explain its launch/verification steps without launching anything. Existing disabled-skill
settings still apply; this installer never changes them. Then try:

> Use cmux-orchestrate to open one visible Claude Code worker in this project's scratch
> worktree. Ask it to inspect the README and suggest one improvement. No edits or external
> writes. Read its result and report whether it actually completed.

See the [worked example](examples/first-worker.md). Use normal workspace trust and permission
controls. Run the controller inside cmux if its socket policy requires that; an external
controller must already have authorized socket access.

## Choose more skills

```sh
python3 install.py --list
python3 install.py --skills cmux-orchestrate autoreview behavior-validator
python3 install.py --skills cmux-orchestrate autoreview behavior-validator --apply
python3 install.py --skills cmux-orchestrate autoreview behavior-validator --check
```

The first selected external skill fetches one pinned `agent-skills` checkout into
`.sources/agent-skills/<commit>/`. Both harnesses link to that same checkout. The manifest
records the owner, public source URL, immutable revision and skill path. The bundled CMUX
skill lives directly in this repository. Keep this checkout at a stable location.

Already have the exact canonical source? Reuse it rather than cloning another copy:

```sh
python3 install.py --skills autoreview behavior-validator \
  --source agent-skills=/absolute/path/to/agent-skills --apply
```

The source binding is remembered for later checks. The checkout must be clean and match the
manifest pin. This tool will not modify that checkout or take ownership of existing skill links.
If another registry already manages a skill, use that registry instead.

[The full catalog](docs/catalog.md) covers **40 capabilities across nine sources**: shared skills,
LifeOS, agent-scripts, Graph Climbing, Humanizer, Waza, GStack, Impeccable and Watch.

The `curated` profile installs 24 capabilities: nine direct skills plus fifteen workflows
behind two routers. Install that compact selection with:

```sh
python3 install.py --profile curated
python3 install.py --profile curated --apply
python3 install.py --profile curated --check
```

For the broader shared selection, `--profile extended` adds Graph Climbing and Humanizer:

```sh
python3 install.py --profile extended
python3 install.py --profile extended --apply
python3 install.py --profile extended --check
```

That installs **26 capabilities through 13 skill folders**, not all 40. The remaining 14 are
selected workflows in Waza, GStack, Impeccable and Watch. Use their [owner installation routes](docs/optional-suites.md):
they have native plugins, generated builds or additional runtime dependencies. The starter
records their provenance but does not silently run their installers or claim to manage them.

`--profile core` selects CMUX, autoreview, behavior-validator and handoff. Profiles add their
selection; switching profiles does not silently remove previously installed skills. Use explicit
uninstall for removal. `--skills` overrides a profile selection. Installing a
skill does not install its tools. In particular, `autoreview` needs its documented reviewer
CLI and secret scanner; read its prerequisites before running it.

## One owner, two projections

Default destinations are `~/.claude/skills/<name>` and `~/.agents/skills/<name>` for Codex.
These are documented personal skill locations, and both support individual symlinked skill
folders: [Claude documentation](https://code.claude.com/docs/en/skills) and
[Codex documentation](https://learn.chatgpt.com/docs/build-skills).

Select one harness with `--harness claude` or `--harness codex`. For a deliberately customized
loader, use `--claude-dir /absolute/loader` or `--codex-dir /absolute/loader`. Existing skills
in Codex's older `~/.codex/skills` directory trigger a collision rather than a duplicate install.
For additional harnesses, check their loader semantics first; only Claude and Codex have
installer targets in this release. Individual skills may need harness-specific adapters.

The installer:

- previews by default and only downloads selected sources with `--apply`;
- refuses existing files, directories, foreign links and modified owned links;
- verifies external revisions and rejects local changes;
- records its own links in a local `.state/links.json` receipt;
- serializes its own writers and rolls back link changes on handled errors;
- leaves source checkouts and unrelated files intact during uninstall.

This is a personal workstation installer, not a hostile-user security boundary or a
power-loss-safe package manager. If interrupted between link creation and receipt writing,
it fails safely on an unowned collision; inspect that link before manually removing it.
It does not rewrite `AGENTS.md`, `CLAUDE.md`, permission settings or existing registries.

## Shared project instructions

Skills provide workflows; the project's instructions decide when and how to use them.
Merge the small [routing snippet](docs/shared-instructions.md) into your existing project
instructions. Keep shared policy in one project-owned document and point both harnesses to it.
Do not overwrite another project's rules or import this repository's maintainer instructions.

LifeOS supplies the broader outcome/verification workflow in the original setup. It is optional
here: this starter works with the direct CMUX skill. [LifeOS integration notes](docs/architecture.md)
explain why simply symlinking its entire runtime into another harness is insufficient.

## Update and uninstall

Review an update before `git pull --ff-only`; bundled skills change with this checkout.
External source pins change only through reviewed edits to `sources.json`. For a reused external
checkout, its owner must update it to that exact revision before this installer can proceed. Run a preview with
the same skill/source selection, apply, then check. Keep old source revisions until you have
verified the update. To roll back, use the prior manifest/checkout version and apply that
selection again. Never edit `.sources` or skill loader links as the canonical source.

```sh
python3 install.py --uninstall --skills cmux-orchestrate autoreview behavior-validator
python3 install.py --uninstall --skills cmux-orchestrate autoreview behavior-validator --apply
```

Repeat the exact harness/destination options you installed with. Uninstall removes only selected
links recorded by this checkout and still pointing to the recorded targets. It keeps downloaded
sources and local state for inspection. A replacement file/link stops removal. Uninstall before
moving or deleting this checkout; a fresh clone cannot claim another clone's links.

## Verification and contributing

```sh
python3 -m unittest discover -s tests -v
python3 install.py --home /absolute/empty/test-home --check
```

The second command should exit 1 on a fresh test home, reporting missing links without writing.
Installer tests use temporary homes, exercise collisions, reuse, drift and removal, and do not
modify real harnesses. See [architecture](docs/architecture.md) for the mapping from the original setup and
[verification](docs/verification.md) for observed runtime coverage.
`--check` proves filesystem/pin consistency, not fresh-session discovery or agent correctness.

Contribute small skills, adapters or tested workflow improvements. Keep one owner per skill,
include provenance, avoid machine-specific defaults, and show a reproducible behavior check.
Never include credentials, private transcripts, customer data or private host inventories.
For DEMOS work, use local fixtures first; repository, network, deployment and transaction
permissions remain with the project owner. This toolkit grants none of them.

MIT licensed. See [NOTICE.md](NOTICE.md) for attribution and dependency licenses.
