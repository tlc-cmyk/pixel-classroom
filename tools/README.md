# Tools

Atlas is rebuilt from CC0 sources in `vendor/src/` (Pixel Office primary).

Rebuild HQ atlas (desks composed with CRT + chairs + shadows, characters 4× outlined):

```bash
python3 tools/build_atlas.py
```

Runtime needs only `index.html` + `assets/atlas.png` + `assets/atlas.json`.
