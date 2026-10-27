
from pathlib import Path


def test_project_has_application_entry_point():
    project_root = Path(__file__).resolve().parents[1]
    app_file = project_root / "src" / "ubuntu_python_desk" / "app.py"

    assert app_file.is_file()
    assert "def main()" in app_file.read_text(encoding="utf-8")
