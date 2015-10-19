import doctest


def suffix_array(text):
    indexes_suff_arr, suff_arr, lbound = [0] * len(text), [0] * len(text), [0] * len(text)
    for i in xrange(len(text)):
        suff_arr[i] = ord(text[i])

    size = 1
    while size <= len(text):
        for i in xrange(len(lbound)):
            if i + size < len(text):
                lbound[i] = ((suff_arr[i], suff_arr[i + size]), i)
            else:
                lbound[i] = ((suff_arr[i], -1), i)
        lbound.sort()
        suff_arr[lbound[0][1]] = 0
        for i in xrange(1, len(lbound)):
            cls, index = lbound[i]
            if cls == lbound[i - 1][0]:
                suff_arr[index] = suff_arr[lbound[i - 1][1]]
            else:
                suff_arr[index] = suff_arr[lbound[i - 1][1]] + 1
        size *= 2

    for i, p in enumerate(suff_arr):
        indexes_suff_arr[p] = i
    return indexes_suff_arr, suff_arr


def lcp(text, _suff_arr_, rank):
    lcp_val = [0] * len(_suff_arr_)
    height = 0
    for i in xrange(len(text)):
        if rank[i] == 0:
            continue
        j = _suff_arr_[rank[i] - 1]
        while text[i + height] == text[j + height]:
            height += 1
        lcp_val[rank[i]] = height
        if height > 0:
            height -= 1
    return lcp_val


def solve(text):
    """
    >>> solve('aacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccbaacbbabbabbbbbaaaaaaabbbbcacacbcabaccaabbbcaaabbccccbbbcbccccbbcaabaaabcbaacbcbaccaaaccbccbcaacbaccb')
    900
    """
    text += chr(0)
    suff_arr, rank = suffix_array(text)
    longest_prefix = lcp(text, suff_arr, rank)
    longest_prefix.append(0)

    result, pref_pos = len(text) - 1, []
    for i, pref_len in enumerate(longest_prefix):
        pos = i
        while pref_pos and pref_pos[-1][1] > pref_len:
            j, h = pref_pos.pop()
            pos = j
            if (i - j + 1) * h > result:
                result = (i - j + 1) * h
        if not pref_pos or pref_pos[-1][1] < pref_len:
            pref_pos.append((pos, pref_len))
    return result


def main():
    print solve(raw_input().strip())


if __name__ == '__main__':
    main()
    doctest.testmod()
