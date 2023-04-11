import click

from commands import shutdown

@click.group()
def start():
    pass

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")

@click.option("--fresh", prompt="Your fresh", help="The person to greet.")
def hello(count, name, fresh):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        # click.echo(f"Hello, {name}!")
        click.echo("pip freeze")
        
start.add_command(hello)
start.add_command(shutdown.shutdown)
start.add_command(shutdown.hibernate)
start.add_command(shutdown.restart)
start.add_command(shutdown.taskkill)

if __name__ == '__main__':
    start()