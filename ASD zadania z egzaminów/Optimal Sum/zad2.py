from zad2testy import runtests
from math import inf



def opt_sum(tab):
    n = len(tab)
    sums = [inf for i in range(n)]
    sums[0] = tab[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + tab[i]

    memo = [[0 for i in range(n)] for j in range(n)]
    memo[0][0] = tab[0]

    for j in range(1, n):
        for i in range(n-1, -1, -1):
            if i == j:
                memo[i][j] = tab[i]
            if i > j:
                memo[i][j] = 0
            if i == j-1:
                memo[i][j] = abs(tab[i] + tab[j])
            if i < j-1:
                if i > 0:
                    memo[i][j] = max(abs(sums[j] - sums[i-1]), min(memo[i+1][j], memo[i][j-1]))
                else:
                    memo[i][j] = max(abs(sums[j]), min(memo[i + 1][j], memo[i][j - 1]))



    return memo[0][n-1]



runtests( opt_sum )
