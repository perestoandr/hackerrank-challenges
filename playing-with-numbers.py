import sys

__author__ = 'Andrey'

if __name__ == '__main__':
    arr_size = input()
    arr = map(int, sys.stdin.readline().strip().split())
    query_size = input()
    query = map(int, sys.stdin.readline().strip().split())

    query_sum = 0
    pos_sum = 0
    pos_num = 0
    neg_list = list()

    for each in arr:
        if each >= 0:
            pos_sum += each
            pos_num += 1
        else:
            neg_list.append(each)
    for query_item in query:
        query_sum += query_item
        tmp = abs(pos_sum + query_sum * pos_num)
        tmp += sum(map(lambda x: abs(x + query_sum), neg_list))
        print tmp