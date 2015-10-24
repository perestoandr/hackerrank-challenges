for _ in input():
    left, right = map(int, raw_input().strip().split())
    if left == 0 or right == 0:
        print "First"
    else:
        optimum_game = max(left, right) - min(left, right) + 1
        if optimum_game % 2 == 0:
            print "First"
        else:
            print "Second"
