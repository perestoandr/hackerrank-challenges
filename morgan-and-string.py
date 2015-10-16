__author__ = 'Andrey Perestoronin'

def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

def solve(f_str, s_str):
    # """
    # >>> solve('abcd', 'bdxyz')
    # 'abbcddxyz'
    # >>> solve('JACK', 'DANIEL')
    # 'DAJACKNIEL'
    # """
    to_first = True
    f_str, s_str = list(f_str[::-1]), list(s_str[::-1])
    result = list()
    while f_str and s_str:
        x, y = f_str.pop(), s_str.pop()
        if x < y:
            result.append(x)
            s_str.append(y)
        elif y < x:
            result.append(y)
            f_str.append(x)
        else:
            ls = list()
            ls.append(''.join(f_str[::-1]))
            ls.append(''.join(s_str[::-1]))
            ls = commonprefix(ls)
            if ls and len(ls) != len(s_str) and len(ls) != len(f_str):
                to_first = f_str[::-1][len(ls)] < s_str[::-1][len(ls)]
            elif (not ls) and (len(f_str) or len(s_str)):

            if to_first:
                result.append(x)
                s_str.append(y)
            else:
                result.append(y)
                f_str.append(x)

    if f_str:
        result = result + f_str[::-1]
    if s_str:
        result = result + s_str[::-1]
    return ''.join(result)


if __name__ == '__main__':
    for _ in xrange(input()):
        print solve(raw_input().strip(), raw_input().strip())
    import doctest
    doctest.testmod()
