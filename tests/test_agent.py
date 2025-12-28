"""Tests for the Resource Scout agent."""

from pathlib import Path

def test_system_prompt_exists():
    prompt_path = Path(__file__).parent.parent / "src" / "ideation_agent_resource_scout" / "prompts" / "system.md"
    assert prompt_path.exists()

def test_cli_import():
    from ideation_agent_resource_scout.main import cli
    assert cli is not None
