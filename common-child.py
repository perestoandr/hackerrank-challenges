__author__ = 'Andrey Perestoronin'


def lcs(f_str, s_str):
    """
    >>> lcs('aab', 'bba')
    1
    >>> lcs('HARRY', 'SALLY')
    2
    >>> lcs('9th9isis99at9es9t', 'testing123testing')
    7
    """
    lengths = [[0 for j in range(len(s_str)+1)] for i in range(len(f_str)+1)]
    # lengths = [[0]*(len(s_str)+1)]*(len(f_str)+1)
    # row 0 and column 0 are initialized to 0
    for i, x in enumerate(f_str):
        for j, y in enumerate(s_str):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
    return lengths[-1][-1]


if __name__ == '__main__':
    print lcs(raw_input().strip(), raw_input().strip())
    import doctest; doctest.testmod()
