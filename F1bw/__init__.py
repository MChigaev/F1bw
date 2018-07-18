import click


def radix_sort(values, key, step=0):
    if len(values) < 2:
        for value in values:
            yield value
        return
    bins = {}
    for value in values:
        bins.setdefault(key(value, step), []).append(value)
    for k in sorted(bins.keys()):
        for r in radix_sort(bins[k], key, step + 1):
            yield r


def bw_key(text, value, step):
    return text[(value + step) % len(text)]


def burroughs_wheeler_custom(text):
    return ''.join(text[i - 1] for i in radix_sort(range(len(text)), partial(bw_key, text)))


def transform(inp):
    inp = inp.lower()
    out = burroughs_wheeler_custom(inp)
    x = 0
    while x < len(out):
        if x != 0 and out[x - 1] == out[x]:
            out = out[0:x - 1] + out[x - 1].upper() + out[x].upper() + out[x + 1:len(out)]
        x += 1
    print(out)


def inverse(inp, endchr):
    inp = inp.lower()
    out = []
    x = 0
    while x < len(inp):
        out.append("")
        x += 1
    x = 0
    while x < len(inp):
        y = 0
        while y < len(inp):
            out[y] = inp[y] + out[y]
            y += 1
        out = sorted(out)
        x += 1
    for z in out:
        if z[len(z) - 1] == endchr:
            out = z
    print(out)


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
