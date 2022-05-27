from unicodedata import numeric
from main import exec_command

N = int(input('How many commands?: '))
arr = []
commands = []
    
for _ in range(N):
    command, *numbers = input('Write your command: ').split(' ')

    if numbers:
        if len(numbers) > 1:
            i, e = numbers

            exec_command(command, arr, int(e), int(i))
        else:
            exec_command(command, arr, numbers.pop())
    else:
        exec_command(command, arr)
