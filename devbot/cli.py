import click
from .github_login import login as login_command
from .github_logout import logout as logout_command
from .config import config as config_commands
from .test import test as test_command


@click.group()
def cli():
    pass


cli.add_command(login_command.login)
cli.add_command(logout_command.logout)
cli.add_command(config_commands.config)
cli.add_command(test_command.test)

