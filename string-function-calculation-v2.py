import doctest


def suffix_array(text):
    indexes_suff_arr, suff_arr, lbound = [0] * len(text), [0] * len(text), [0] * len(text)
    for ind in xrange(len(text)):
        suff_arr[ind] = ord(text[ind])

    size = 1
    while size <= len(text):
        for ind in xrange(len(lbound)):
            if ind + size < len(text):
                lbound[ind] = ((suff_arr[ind], suff_arr[ind + size]), ind)
            else:
                lbound[ind] = ((suff_arr[ind], -1), ind)
        lbound.sort()
        suff_arr[lbound[0][1]] = 0
        for ind in xrange(1, len(lbound)):
            cls, index = lbound[ind]
            if cls == lbound[ind - 1][0]:
                suff_arr[index] = suff_arr[lbound[ind - 1][1]]
            else:
                suff_arr[index] = suff_arr[lbound[ind - 1][1]] + 1
        size *= 2

    for ind, p in enumerate(suff_arr):
        indexes_suff_arr[p] = ind
    return indexes_suff_arr, suff_arr


def lcp(text, _suff_arr_, rank):
    lcp_val = [0] * len(_suff_arr_)
    height = 0
    for ind in xrange(len(text)):
        if rank[ind] == 0:
            continue
        j = _suff_arr_[rank[ind] - 1]
        while text[ind + height] == text[j + height]:
            height += 1
        lcp_val[rank[ind]] = height
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
