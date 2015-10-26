from fractions import gcd
from itertools import product
from numpy import array
import numpy as np

__author__ = 'Andrey'
for _ in xrange(input()):
    n, result_needed = map(int, raw_input().strip().split())
    num_range = array(xrange(1, n + 1, 1))
    prod_list = product([1, -1], repeat=n)
    answer = "NO"
    for prod in prod_list:
        k = np.sum(num_range * prod)
        if k == result_needed:
            answer = "YES"
            break

    print np.sum(num_range)
    if gcd(np.sum(num_range), result_needed) != 1:
        if gcd(np.sum(num_range), result_needed) == result_needed:
            print gcd(np.sum(num_range), result_needed)
            print "yay"
    print answer
