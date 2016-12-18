import click
import bzapi

def print_bugs(bugs):
    click.echo(bzapi.summarize_bugs(bugs))

@click.group()
def cli():
    pass

@cli.command()
@click.option('--start-date', default=bzapi.get_start_day(),
              help="First day to consider when looking for recent bugs")
def recent(start_date):
    """Gets recently modified bugs relevant to :harter"""
    print_bugs(bzapi.get_recently_active_bugs(start_date))


@cli.command()
def next():
    """Gets P1 bugs assigned to :harter, i.e. next week's work"""
    print_bugs(bzapi.get_current_bugs())


if __name__ == "__main__":
    cli()
