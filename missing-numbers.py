from collections import Counter


def check(_a, _b):
    result_list = list()
    count_a = Counter(_a)
    count_b = Counter(_b)
    for each in count_b:
        if count_b[each] != count_a[each]:
            result_list.append(each)
    return ' '.join(map(str, result_list))


if __name__ == '__main__':
    len_a = input()
    a = map(int, raw_input().strip().split())
    len_b = input()
    b = map(int, raw_input().strip().split())
    print check(a, b)
