"""CLI script for the 3R-project-repo package. This will be called on the command line"""

import click

from 3R-project-repo.3R-project-repo import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def 3R-project-repo_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
