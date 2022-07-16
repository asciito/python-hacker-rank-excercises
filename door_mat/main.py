def door_mat(n, m):    
    output = [('.|.' * odd).center(m, '-') for odd in range(1, n, 2)]
    return '\n'.join([
        *output,
        'WELCOME'.center(m, '-'),
        *( list(reversed(output)) )
    ])