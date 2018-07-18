@click.command()
@click.option("-t", is_flag=True, help="Specifies that a transformation is needed.")
@click.option("-i", is_flag=True, help="Specifies that an inverse is needed.")
@click.option("--string", prompt="String", help="The string to be transformed, or the string to have the inverse run on it.")
@click.option("--endchr", default="%", help="The end character, only used for the inverse operation. The default character is %", required=False)
def main(t, i, string, endchr):
    """Program that transforms or performs the inverse of a Burrows-Wheeler 
    Transform on a given string. 
    If the operation was a transformation, 
    the program then looks for repeats and highlights them by capitalizing them. 
    It is also case insensitive."""
    if t and i:
        print("You cannot transform and perform an inverse at the same time. See --help")
        return
    if t:
        transform(string)
    elif i:
        if endchr not in string:
            print("The end character must be in the string that is to have the inverse applied to it. The default end character is %. See --help")
            return
        inverse(string, endchr)
    else:
        print("A transformation must be specified, see --help.")


main()
