_v = ['A', 'E', 'I', 'O', 'U']
_c = [chr(n).upper() for n in range(65, 91) if chr(n).upper() not in _v]

def count_words_starts_with(string, start_with_vowel=False) -> int:
    c = 0
    l = len(string)

    for i, sub in enumerate(string):
        if sub not in (_v if start_with_vowel else _c):
            continue
        c += l - i

    return c

def minion_game(string: str) -> str:
    stuart_points = count_words_starts_with(string)
    kevin_points = count_words_starts_with(string, True)

    if stuart_points > kevin_points:
        return f'Stuart {stuart_points}'
    elif stuart_points < kevin_points:
        return f'Kevin {kevin_points}'
    else:
        return 'Draw'