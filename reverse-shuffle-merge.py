from collections import defaultdict


def solve(_str_):
    _str_ = _str_[::-1]
    count = defaultdict(int)
    for letter in _str_:
        count[letter] += 1
    need = defaultdict(int)
    for c in count:
        need[c] = count[c] / 2

    solution = list()
    i = 0
    while len(solution) < len(_str_) / 2:
        min_char_index = -1
        while True:
            char = _str_[i]
            if need[char] > 0 and (min_char_index < 0 or char < _str_[min_char_index]):
                min_char_index = i
            count[char] -= 1
            if count[char] < need[char]:
                break
            i += 1

        for j in range(min_char_index + 1, i + 1):
            count[_str_[j]] += 1

        need[_str_[min_char_index]] -= 1
        solution.append(_str_[min_char_index])

        i = min_char_index + 1
    return ''.join(solution)


if __name__ == '__main__':
    print solve(raw_input())
