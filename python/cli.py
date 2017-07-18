import click
import bzapi


def print_bugs(bugs):
    click.echo(bzapi.summarize_bugs(bugs))

def get_api_key(ctx):
    key = 'API_KEY'
    if key in ctx.obj:
        return ctx.obj[key]
    else:
        return ""

@click.group()
@click.option('--api_key', envvar='BUGZILLA_API_KEY', type=click.File('r'))
@click.pass_context
def cli(ctx, api_key):
    if api_key is not None:
        ctx.obj['API_KEY'] = api_key.read()


@cli.command()
@click.option('--start-date', default=bzapi.get_start_day(),
              help="First day to consider when looking for recent bugs")
@click.pass_context
def recent(ctx, start_date):
    """Gets recently modified bugs relevant to :harter"""
    print_bugs(bzapi.get_recently_active_bugs(
        start_date,
        api_key = get_api_key(ctx)
    ))


@cli.command()
@click.pass_context
def next(ctx):
    """Gets P1 bugs assigned to :harter, i.e. next week's work"""
    print_bugs(bzapi.get_current_bugs(api_key=get_api_key(ctx)))


if __name__ == "__main__":
    cli(obj={})
