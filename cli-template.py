import click
import stuff

# Define a bunch of functions


@click.command()
@click.argument("argument")
@click.option("--option")
def main(argument, option):
    """Description of command"""
    # Call that bunch of functions to perform the command


if __name__ == "__main__":
    # If the script is executed at the command line
    # Just call the main function, click handles the arguments
    main()