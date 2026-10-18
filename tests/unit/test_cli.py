from importlib.metadata import version

from typer.testing import CliRunner

from learntopia.cli import app

runner = CliRunner()


def test_command_prints_version() -> None:
    expected = version("learntopia")
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert expected in result.output
