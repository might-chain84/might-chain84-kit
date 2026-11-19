import json
import tempfile
from pathlib import Path

from might_chain84_kit.core import MightChain84Tool


def test_valid_json_is_normalized():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "a.json")
        path.write_text('{"b": 1, "a": 2}', encoding="utf-8")
        ok, payload = MightChain84Tool().check(path)
        assert ok
        assert json.loads(payload) == {"a": 2, "b": 1}


def test_missing_file_is_reported():
    ok, reason = MightChain84Tool().check("/no/such/file.json")
    assert not ok and reason == "file not found"


def test_broken_json_reports_position():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "bad.json")
        path.write_text("{", encoding="utf-8")
        ok, reason = MightChain84Tool().check(path)
        assert not ok and "invalid JSON" in reason
