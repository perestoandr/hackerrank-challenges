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
    # debug
    # for each in lengths:
    #     print each
    # read the substring out from the matrix
    result = list()
    x, y = len(f_str), len(s_str)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            assert f_str[x - 1] == s_str[y - 1]
            result.append(f_str[x - 1])
            x -= 1
            y -= 1
    #return "".join(result[::-1]) to print subsequence
    return len(result)


if __name__ == '__main__':
    print lcs(raw_input().strip(), raw_input().strip())
    import doctest; doctest.testmod()
