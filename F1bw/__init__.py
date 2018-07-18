import sys


import click
from core import transform
from core import inverse


@click.command()
@click.option("-f", is_flag=True, help="Transforms forward a string.")
@click.option("-i", is_flag=True, help="Does the inverse on a string.")
@click.option("--string", prompt="String", help="The string to be transformed, or the string to have the inverse run on it.")
@click.option("--endchr", default="%", help="The end character, only used for the inverse operation. The default character is %", required=False)
def main(t, i, string, endchr):
    """
    Transforms forward or does the inverse on a string.
    :param t: t is a boolean which tells the function to run the transform function.
    
    :param i: i is a boolean which tells the function to run the inverse function.
    
    :param string: the string is the text that is supplied to either transform or have the inverse run on it.
    
    :param endchr: the endchr is the end character that is supplied to determine the original string when running the inverse.
    """
    if t and i:
        print("You cannot transform and perform an inverse at the same time. See --help.")
        sys.exit(1)
    if t:
        transform(string)
        sys.exit(0)
    elif i:
        if endchr not in string:
            print("The end character must be in the string that is to have the inverse applied to it. The default end character is %. See --help")
            sys.exit(1)
        inverse(string, endchr)
        sys.exit(0)
    else:
        print("A transformation must be specified, see --help.")
        sys.exit(1)
if __name__ == "__main__":
    main()
