from zad1testy import runtests
from math import inf

def zbigniew( A ):
    n = len(A)
    max_energy = 0
    for i in range(n):
        max_energy += A[i]

    memo = [[inf for i in range(n)]for j in range(max_energy + 1)]
    memo[A[0]][0] = 0

    for i in range(1, n):
        min_curr_energy = A[i]
        for j in range(max_energy + 1):
            for k in range(i-1, -1, -1):
                if j + i-k > max_energy or j + min_curr_energy > max_energy + 1:
                    break
                if memo[j + i-k][k] < inf:
                    if memo[j + i-k][k] + 1 < memo[j + min_curr_energy][i]:
                        memo[j + min_curr_energy][i] = memo[j + i-k][k] + 1


    minimum = inf

    for i in range(max_energy + 1):
        if memo[i][n - 1] < minimum:
            minimum = memo[i][n - 1]

    if minimum == inf:
        return -1
    return minimum


runtests( zbigniew ) 
