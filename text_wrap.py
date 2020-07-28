

def wrap(string, max_width):
    string = textwrap.wrap(string, max_width)
    return "\n".join(string)

