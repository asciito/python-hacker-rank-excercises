def capitalize(name: str) -> str:
    """
    [Summary]

    Begin every first word with their capital letter

    [Arguments]:
        :name str: The full name to capitalize
    """

    result = []
    fullName = name.strip().split(' ')

    for s in fullName:
        if not s or len(s) == 1:
            result.append(s.upper())
        else:
            result.append(s[0].upper() + s[1:])

    return ' '.join(result)