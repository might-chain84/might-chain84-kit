# might-chain84-kit

Validate JSON files and print a normalized form.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m might_chain84_kit.cli --help
```

```python
from might_chain84_kit.core import MightChain84Tool

tool = MightChain84Tool()
print(tool)
```

## Layout

```
might_chain84_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 might-chain84
