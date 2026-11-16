# Project working instructions

- This is the user's IELTS Academic Studio project at `D:/english`, published from `yann531/ielts-academic-studio`, branch `main`.
- After completing an authorized code or content update, the user's default preference is to commit and push the project changes to GitHub and verify the existing Pages workflow. Do not stop at a local-only delivery unless the current request explicitly says not to commit, push, or publish. A later explicit restriction overrides this default.
- Preserve remote changes; fetch and integrate them before pushing. Do not force-push shared history.
- Sync project code and public learning content only. Never commit browser learning records, personal backups, recordings, private materials, credentials, `private/`, dependencies, or local release archives. Learning data stays in the existing browser IndexedDB and remains backup-compatible.
- Keep the core limited to IELTS Academic and usable without paid APIs, a server, or an account system.
- Use pnpm 10. The local pinned runner is `node .tools/pnpm10/package/bin/pnpm.cjs`; do not switch this checkout to pnpm 11 or npm. Validate relevant changes with the existing tests, content checks, and production build.
- Curated vocabulary sources live in `content/vocabulary/`; regenerate with `python -X utf8 scripts/curate-vocabulary.py`. Preserve existing vocabulary IDs and document source/coverage limits honestly.
