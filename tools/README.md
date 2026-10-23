# Tools

Atlas is built offline from CC0 sources in `vendor/src/` (Pixel Office, Kenney Indoor, office appliances).

Rebuild (optional):

```bash
# sources already under vendor/src/
python3 - <<'PY'
# see agent build script history / assets/CREDITS.md
print('Re-run the build atlas script from the project history if regenerating.')
PY
```

Runtime needs only `index.html` + `assets/atlas.png` + `assets/atlas.json`.
