from pathlib import Path
import pytest


@pytest.fixture
def specs_root() -> Path:
    return Path(__file__).parent / "specs"
