def GoodThief(T):
    n = len(T)
    memo = [0 for i in range(n)]
    memo[0] = T[0]
    memo[1] = T[1]
    for i in range(2, n):
        for j in range(i-2, 0, -1):
            if T[i] + memo[j] > memo[i]:
                memo[i] = T[i] + memo[j]

    return max(memo)

T = [1, 3, -1, 0, 2, -1, 5, 1]
print(GoodThief(T))
