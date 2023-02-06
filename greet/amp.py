import click
"""
DCP CLI helps to fetch information from a codified app metadata
"""

@click.group()
def cli():
    """ 
    DCP CLI to fetch App Metadata
    """
    pass


@cli.command()
@click.option('--service', '-s', help='name of the service to select.')
@click.option('--owner', '-m', help='name of the service owner to select.')
def list_services(service,owner):
    """ 
    Fetches services from Appmetadata. Also supports filters to choose based on service's name and/or owner's name
    """
    click.echo('\nfetches the list of services from app metadata json\n')
    if service:
      click.echo(f"service filtered is {service}\n")
    if owner:
      click.echo(f"owner filtered is {owner}\n")


@cli.command()
def list_owners():
    """ 
    Fetches owners from Appmetadata. Also supports filters based on switches
    """
    click.echo('fetches the owners\' info from app metadata json\n')


if __name__ == '__main__':
    cli()
