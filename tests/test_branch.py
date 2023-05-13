from typer.testing import CliRunner
from branch_time.jira import app
runner = CliRunner()


def test_result_lost_by_show_with_luck():
    result = runner.invoke(app, ["any_where", "--time", "1"])
    assert result.exit_code == 1
    assert "Directory not found" in result.output
