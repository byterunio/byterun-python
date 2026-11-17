import subprocess
import sys
import zipfile
from importlib import metadata
from pathlib import Path

import byterun

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_VERSION = "0.0.1"


def test_import_and_version():
    assert byterun.__version__ == EXPECTED_VERSION


def test_installed_metadata():
    meta = metadata.metadata("byterun")
    assert meta["Name"] == "byterun"
    assert meta["Version"] == EXPECTED_VERSION
    assert meta["Requires-Python"] == ">=3.10"
    assert meta["License-Expression"] == "Apache-2.0"
    assert metadata.requires("byterun") is None  # no runtime dependencies
    urls = meta.get_all("Project-URL")
    assert any(u.startswith("Homepage, https://byterun.io/") for u in urls)


def test_wheel_contains_package(tmp_path):
    subprocess.run(
        [sys.executable, "-m", "build", "--wheel", "--no-isolation", "--outdir", str(tmp_path), str(ROOT)],
        check=True,
        capture_output=True,
    )
    (wheel,) = tmp_path.glob("byterun-*.whl")
    assert wheel.name.startswith(f"byterun-{EXPECTED_VERSION}-")
    with zipfile.ZipFile(wheel) as zf:
        names = zf.namelist()
    assert "byterun/__init__.py" in names
    assert not any(n.startswith(("tests/", "src/")) for n in names)
