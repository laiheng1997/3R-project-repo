"""CLI script for the 3R_project_repo package. This will be called on the command line"""

import click

from 3R_project_repo.3R_project_repo import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def 3R_project_repo_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
