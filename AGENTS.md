# Maintainer instructions

This repository owns the installer, portable CMUX adapter, source manifest and public docs.
External skills retain their upstream owners. Do not edit downloaded `.sources` contents.

Use Python 3.10+ and the standard library. Preview loader changes; never apply tests to a real
home directory. Preserve existing files and foreign links. Run the unittest suite and
`git diff --check`. Keep user data, credentials and local installation receipts out of Git.

Do not claim runtime discovery from symlink tests alone. Document the exact observed coverage.
