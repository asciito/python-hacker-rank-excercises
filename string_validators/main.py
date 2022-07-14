def string_validators(S: str) -> list[bool]:
    result: list[bool] = [False for _ in range(5)] # [False, False, False, False, False]

    for c in S:
        if c.isalnum() and not result[0]:
            result[0] = True

        if c.isalpha() and not result[1]:
            result[1] = True

        if c.isdigit() and not result[2]:
            result[2] = True

        if c.islower() and not result[3]:
            result[3] = True
        
        if c.isupper() and not result[4]:
            result[4] = True


    return result