import click
import bzapi


def print_bugs(bugs):
    click.echo(bzapi.summarize_bugs(bugs))

@click.group()
@click.option('--api_key', envvar='BUGZILLA_API_KEY', type=click.File('r'))
@click.pass_context
def cli(ctx, api_key):
    ctx.obj['API_KEY'] = api_key.read()


@cli.command()
@click.option('--start-date', default=bzapi.get_start_day(),
              help="First day to consider when looking for recent bugs")
@click.pass_context
def recent(ctx, start_date):
    """Gets recently modified bugs relevant to :harter"""
    print_bugs(bzapi.get_recently_active_bugs(
        start_date,
        api_key = ctx.obj['API_KEY']
    ))


@cli.command()
@click.pass_context
def next(ctx):
    """Gets P1 bugs assigned to :harter, i.e. next week's work"""
    print_bugs(bzapi.get_current_bugs(api_key=ctx.obj['API_KEY']))


if __name__ == "__main__":
    cli(obj={})
