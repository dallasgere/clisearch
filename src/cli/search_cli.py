import click
from rich.console import Console


class SearchCli:
    def __init__(self):
        self.console = Console()

    @click.group
    def cli(self):
        """
        the cli group to keep track of commands in the SearchCli class
        """
        pass

    @cli.command
    def search(self):
        pass
