__author__ = 'Andrey'


def count_down(dim, steps, height):
    result = 0
    if height == 0 and steps == 0:
        return 1
    if height < 1 or steps < 0:
        if steps < 1:
            return 0
        # result += count_down(dim, steps - 1, height - 1)
        for i in xrange(steps % 2, steps + 1, 2):
            result += dim ** i
    else:
        result += dim ** steps + count_down(dim, steps - 1, height - 1)
    return int(result)


def count_down_non_recursive(dim, steps, height):
    result = 0

    for s in range(steps - height + 1, steps + 1, 1):
        result += int(dim ** s)
        steps -= 1
        height -= 1
    for i in range(steps % 2, steps + 1, 2):
        result += int(dim ** i)
    return result


if __name__ == '__main__':
    for _ in xrange(input()):
        d, k, h = map(int, raw_input().strip().split())
        print count_down_non_recursive(d, k, h) % (10 ** 9 + 7)
