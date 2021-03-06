from typer.testing import CliRunner

from inventopy.__main__ import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
