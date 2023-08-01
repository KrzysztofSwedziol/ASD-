from egz1btesty import runtests
from math import inf

def planets( D, C, T, E ):
    n = len(D)
    memo = [[inf for i in range(n)] for j in range(E+1)]
    memo[0][0] = 0
    for k in range(E + 1):
        memo[k][0] = C[0] * k

    planet = T[0][0]
    cost = T[0][1]
    memo[0][planet] = cost + memo[0][0]

    for i in range(1, n):
        for j in range(E + 1):
            prev_to_curr = D[i] - D[i-1]
            if j + prev_to_curr < E :
                first_option = memo[j + prev_to_curr][i-1]
            if j + prev_to_curr >= E :
                first_option = memo[E][i-1] + C[i]*(j - (E - prev_to_curr))
            if j-1 >= 0 :
                second_option = memo[j-1][i] + C[i] * 1
            if j-1 < 0 :
                second_option = inf

            memo[j][i] = min(memo[j][i], first_option, second_option)
            if j == 0:
                planet = T[i][0]
                cost = T[i][1]
                if memo[0][planet] > cost + memo[j][i]:
                    memo[0][planet] = cost + memo[j][i]

    return memo[0][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
