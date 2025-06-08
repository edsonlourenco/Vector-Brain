"""Test cases for utils.settings module."""

from utils.settings import Session


def test_pdf_path_default():
    session = Session()
    assert session.PDF_PATH == "docs/Databricks_LLM_guide_ptbr.pdf"

def test_openai_api_key_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key-123")
    session = Session()
    assert session.OPENAI_API_KEY == "fake-key-123"

def test_openai_api_key_none(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    session = Session()
    assert session.OPENAI_API_KEY is None