# Contributing

Contributions are welcome, especially:

- New reusable scene manifests.
- Better edge-matte and despill algorithms.
- Reproducible fixes for text, naming, or validation failures.
- Documentation for additional agent runtimes.

## Development

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python skills/sticker-pack-maker/scripts/sticker_pipeline.py --help
```

Keep the Skill instructions concise. Put detailed patterns in `references/` and reusable templates in `assets/`.

Do not submit private portraits, copyrighted character artwork, API keys, or generated assets you do not have permission to redistribute.
