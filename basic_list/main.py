def exec_command(command: str, arr: list, value: int = None, index: int = None):
    if command == 'insert':
        arr.insert(index, value)
    elif command == 'print':
        print(arr)
    elif command == 'remove':
        arr.remove(value)
    elif command == 'append':
        arr.append(value)
    elif command == 'sort':
        arr.sort()
    elif command == 'pop':
        arr.pop()
    elif command == 'reverse':
        arr.reverse()
    else:
        pass