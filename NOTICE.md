# Provenance and credits

This repository contains an original small installer and harness adapters. It applies the
single-owner/shared-projection architecture used by the maintainer's Claude/Codex setup.
It does not redistribute private setup files or imply endorsement by upstream projects.

## Pinned sources

| Source owner | Revision | License |
|---|---|---|
| [agent-skills integration fork](https://github.com/mj-deving/agent-skills), based on [openclaw/agent-skills](https://github.com/openclaw/agent-skills) | `7d4d219626c46d3c1d664a5a3e2206ed2cfd623e` | MIT; copyright 2026 openclaw |
| [LifeOS — Daniel Miessler](https://github.com/danielmiessler/LifeOS) | `be9e8ef889f00a29f4fd677dee4772fdf32e07ce` (7.40.4) | MIT; copyright 2025–2026 Daniel Miessler |
| [agent-scripts — Peter Steinberger](https://github.com/steipete/agent-scripts) | `c46ea65b6323e8a2b6f441f8b6449ae731bc8f81` | MIT; copyright 2026 Peter Steinberger |

The installer checks out these sources without modifying their bodies and retains their
LICENSE files and attribution. Their licenses apply to their respective contents.
The portable CMUX skill draws on [LifeOS CMUX](https://github.com/danielmiessler/LifeOS/tree/be9e8ef889f00a29f4fd677dee4772fdf32e07ce/LifeOS/install/skills/CMUX)
and the documented cmux CLI, with independent portability and verification instructions.
The LifeOS license notice below is retained for this adaptation.

cmux is a separately installed application, not bundled code. See its
[repository and licensing](https://github.com/manaflow-ai/cmux) and [CLI reference](https://cmux.com/docs/api).
Claude Code and Codex remain separately installed products under their respective terms.

## LifeOS MIT notice

Copyright (c) 2025-2026 Daniel Miessler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Additional sources in the extended selection

- [Graph Climbing](https://github.com/mj-deving/graph-climbing), `192d7785fc969c1f69634927a23bd2433715b23b`, MIT.
- [Humanizer integration fork](https://github.com/mj-deving/humanizer), `d4fed7bd33a1bb59d2ca4f3a27816ec17b7d4ee6`, MIT; retains its upstream attribution.
- [Waza](https://github.com/tw93/Waza), `663f27eb136118c0a3aa78b5ce9e712b7aee7f0a`: optional native/vendor-owned suite.
- [GStack](https://github.com/garrytan/gstack), `0d1bd5616c0ef096bb7ccee336f63c60ee408618`: optional vendor-owned suite.
- [Impeccable](https://github.com/pbakaus/impeccable), `f2c7051853848826aac2f4646581d62a732155ad`: optional vendor-owned suite, Apache-2.0.
- [Watch / claude-video](https://github.com/bradautomates/claude-video), `83da59fa78c3eee9e20f515fe75c438bb5166efd`: optional upstream skill, MIT.

No code or skill bodies from the four optional suites are redistributed here. Their reviewed pins
identify the catalog snapshot; their native installers may install newer releases. Check the
version and license selected by that installer before adopting it.
