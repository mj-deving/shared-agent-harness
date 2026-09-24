# Optional suites: keep their own installers

The full catalog lists 40 selected capabilities. The shared installer manages 26; the other 14
are Waza's eight workflows, four selected GStack modules, Impeccable and Watch. These are optional
additions, not dependencies of CMUX. `install.py --check` does not verify their installation.

The pinned links below identify the reviewed source snapshot. Native installers may select a
newer release; inspect the version and instructions they present. Do not install the same suite
through two owners or copy a plugin cache into this repository.

## Waza

**Recommended: keep Waza standalone as the official plugin.** It already packages its eight
workflows and owns their updates. There is no Waza body, wrapper or loader link in this starter.

In Claude Code's command input:

```text
/plugin marketplace add tw93/Waza
/plugin install waza@waza
```

For Codex's CLI, the [reviewed upstream instructions](https://github.com/tw93/Waza/blob/663f27eb136118c0a3aa78b5ce9e712b7aee7f0a/README.md#install) give:

```sh
codex plugin marketplace add tw93/Waza
codex plugin add waza@waza
```

Use the plugin manager's current help if your version differs. Open a fresh session and verify
its eight names: think, hunt, check, health, learn, read, write and ui. Keep updates/removal with
the same plugin manager. Do not also install Waza through this starter or a second skill manager.

The author's larger setup shares a native plugin source with another harness through an adapter.
That private runtime coupling is not a prerequisite here: each user's official plugin manager
owns its projection. Same upstream owner does not require byte-identical runtime caches.

## GStack

Use [GStack's installation and host instructions](https://github.com/garrytan/gstack/tree/0d1bd5616c0ef096bb7ccee336f63c60ee408618#install--30-seconds).
It requires its build/runtime dependencies and produces harness-specific skill outputs. For
Codex, follow the upstream `--host codex` path; Claude uses its native suite setup. Keep one suite
source and let its owner generate the appropriate outputs rather than hand-linking raw leaves.

Our four picks are plan-ceo-review, plan-eng-review, qa and ship. Upstream may install a larger
suite. Review its proposed instruction edits, hooks and update behavior before opting in; do not
replace an existing browser policy or registry simply because the vendor example does so.
A shipping skill being installed does not authorize publishing or deployment.

## Impeccable

Use the [Impeccable installer](https://github.com/pbakaus/impeccable/tree/f2c7051853848826aac2f4646581d62a732155ad#installation):

```sh
npx impeccable install
```

Choose the intended project/global scope and harnesses interactively. It generates provider
outputs and may add project-local hooks; keep their trust and lifecycle with that owner. Start
with `/impeccable init` only in a project where creating design context is authorized. Its source
uses Apache-2.0; that license is separate from this starter's MIT license.

## Watch

Use the [public Watch skill](https://github.com/bradautomates/claude-video/tree/83da59fa78c3eee9e20f515fe75c438bb5166efd#watch).
For Claude Code, its official plugin route is:

```text
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

For Codex and other supported Agent Skills hosts, upstream documents `npx skills add
bradautomates/claude-video -g`. Select only the harnesses you intend to use; keep that skill
manager as the owner. Do not combine this with a competing installation of the same skill.

Video analysis needs media tools such as yt-dlp and ffmpeg. The upstream workflow can offer or
perform dependency installation; inspect that setup before its first run. Captions may suffice;
transcription fallback can require provider credentials and incur cost. This starter neither
installs those tools nor exports the author's private credential-handling adapter. Use your own
approved credential mechanism and only recordings you are authorized to access.

## Verify after opting in

Open a fresh session in each selected harness. Confirm the intended names and source owner,
then run one small representative task. Verify actual browser/media/reviewer behavior where the
workflow needs it. File presence, plugin installation and a completed user task are distinct
claims. None of these optional suites has been installed or exercised by this starter's tests.
