def occurrence(string: str, sub: str) -> str:
    start = count = 0

    while True:
        start = string.find(sub, start) + 1

        if start > 0:
            count += 1
        else:
            break

    return count

def countIn(string: str, allowed='consonants') -> int:
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = [chr(n).upper() for n in range(65, 91) if chr(n).upper() not in vowels]
    words = {}

    for i, sub in enumerate(string):
        
        if sub not in (consonants if allowed == 'consonants' else vowels):
            continue

        if not words.get(sub):
            words[sub] = occurrence(string, sub)

        for c in string[i + 1:]:
            sub += c # The new substring

            if not words.get(sub):
                words[sub] = occurrence(string, sub)

    return sum(words.values())

def minion_game(string: str) -> str:
    stuart_points = countIn(string)
    kevin_points = countIn(string, 'vowels')

    if stuart_points > kevin_points:
        return f'Stuart {stuart_points}'
    elif stuart_points < kevin_points:
        return f'Kevin {kevin_points}'
    else:
        return 'Draw'