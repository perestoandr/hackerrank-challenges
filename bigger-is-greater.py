"""
Problem:
https://www.hackerrank.com/challenges/bigger-is-greater
"""


def next_permutation(str_list):
    i = len(str_list) - 2
    while not (i < 0 or str_list[i] < str_list[i + 1]):
        i -= 1
    if i < 0:
        return False
    j = len(str_list) - 1
    while not (str_list[j] > str_list[i]):
        j -= 1
    str_list[i], str_list[j] = str_list[j], str_list[i]
    str_list[i + 1:] = reversed(str_list[i + 1:])
    return True


if __name__ == '__main__':
    for i in xrange(input()):
        common_str_list = list(raw_input().strip())
        if next_permutation(common_str_list):
            print ''.join(common_str_list)
        else:
            print 'no answer'
