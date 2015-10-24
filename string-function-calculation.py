import doctest


def count_matches(text, pattern):
    # """
    # >>> count_matches('aaaaaa','aaa')
    # 4
    # >>> count_matches('aaaaaa','aa')
    # 5
    # """
    count = start = 0
    while True:
        start = text.find(pattern, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def func(_str, substr):
    # """
    # >>> func('aaaaaa','aaa')
    # 12
    # >>> func('aaaaaa','aa')
    # 10
    # """
    return len(substr) * count_matches(_str, substr)


def solve(_str_):
    """
    >>> solve('aacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccb')
    900
    """
    maximum = set()
    for i in xrange(1, len(_str_) + 1, 1):
        sub = _str_[:i]
        maximum.add(func(_str_, sub))

    return max(maximum)


if __name__ == "__main__":
    print solve(raw_input().strip())
    doctest.testmod()
