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


def string_similarity(a):
    result = 0
    return result


if __name__ == '__main__':
    for i in range(input()):
        print string_similarity(raw_input().strip())
