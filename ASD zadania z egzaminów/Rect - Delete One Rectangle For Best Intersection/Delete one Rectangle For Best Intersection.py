from zad1testy import runtests

def area(rectangle):
    left_side, floor, right_side, ceiling = rectangle
    return (right_side - left_side) * (ceiling - floor)

def common_of_two(rectangle1, rectangle2):
    x1_1, y1_1, x2_1, y2_1 = rectangle1
    x1_2, y1_2, x2_2, y2_2 = rectangle2

    new_x1 = max(x1_1, x1_2)
    new_y1 = max(y1_1, y1_2)
    new_x2 = min(x2_1, x2_2)
    new_y2 = min(y2_1, y2_2)

    if new_x1 < new_x2 and new_y1 < new_y2:
        return [new_x1, new_y1, new_x2, new_y2]
    else:
        return [0, 0, 0, 0]

def rect(D):
    n = len(D)
    memo = []

    # first slide (from start to end)
    memo.append([float('-inf'), float('-inf'), float('inf'), float('inf')])
    memo.append(D[0])
    common_left = D[0]
    for i in range(1, n):
        common_left = common_of_two(common_left, D[i])
        memo.append(common_left)

    # second slide (from end to start)
    common_right = D[n - 1]
    memo[n - 2] = common_of_two(memo[n - 2], D[n - 1])
    for j in range(n - 3, -1, -1):
        common_right = common_of_two(common_right, D[j+1])
        memo[j] = common_of_two(memo[j], common_right)

    # change to areas
    max_ind = 0
    max_area = 0
    for k in range(n):
        memo[k] = area(memo[k])
        if memo[k] > max_area:
            max_area = memo[k]
            max_ind = k

    return max_ind

    
runtests( rect )


