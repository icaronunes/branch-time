from typer.testing import CliRunner
from branch_time.jira import app
runner = CliRunner()


def test_not_directory():
    result = runner.invoke(app, ["any_where", "--time", "1"])
    assert result.exit_code == 1
    assert "Directory not found" in result.output

def test_not_directory_on_git():
    result = runner.invoke(app, ["../../", "--time", "1"])
    assert result.exit_code == 1
    assert "repository parameter does not point to a git repository" in result.output
