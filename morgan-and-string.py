__author__ = 'Andrey Perestoronin'


def solve(f_str, s_str):
    """
    >>> solve('abcd', 'bdxyz')
    'abbcddxyz'
    """
    f_str, s_str = list(f_str[::-1]), list(s_str[::-1])
    result = list()
    while f_str and s_str:
        x, y = f_str.pop(), s_str.pop()
        if x < y:
            result.append(x)
            s_str.append(y)
        else:
            result.append(y)
            f_str.append(x)
    if (f_str): result = result + f_str[::-1]
    if (s_str): result = result + s_str[::-1]
    return ''.join(result)

if __name__ == '__main__':
    for _ in xrange(input()):
        print solve(raw_input().strip(), raw_input().strip())
    import doctest; doctest.testmod()