from fractions import gcd
from math import sqrt


def triangle_square(_A, _B, _C):
    double_s = (_A[0] - _C[0])*(_B[1] - _C[1]) - (_B[0] - _C[0])*(_A[1] - _C[1])
    return abs(double_s)


def picks_get_inside_dots(_A, _B, _C):
    border_dots = 0
    tri_square = triangle_square(_A, _B, _C)
    # [A,B]
    border_dots += gcd(abs(_B[0] - _A[0]), abs(_B[1] - _A[1])) + 1
    # [A,C]
    border_dots += gcd(abs(_C[0] - _A[0]), abs(_C[1] - _A[1])) + 1
    # [B,C]
    border_dots += gcd(abs(_C[0] - _B[0]), abs(_C[1] - _B[1])) + 1

    border_dots -= 3

    inside_dots_result = (tri_square - border_dots + 2)/2

    return inside_dots_result


for _ in xrange(input()):
    point_list = map(int, raw_input().strip().split())
    A = [point_list[0], point_list[1]]
    B = [point_list[2], point_list[3]]
    C = [point_list[4], point_list[5]]

    print picks_get_inside_dots(A, B, C)
