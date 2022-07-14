def wrap(string, max_width):
    if len(string) <= max_width:
        return string

    return string[:max_width] + "\n" + wrap(string[max_width:], max_width)

