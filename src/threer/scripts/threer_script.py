"""CLI script for the threer package. This will be called on the command line"""

import click

from threer.threer import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def threer_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
