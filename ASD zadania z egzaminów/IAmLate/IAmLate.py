from zad3testy import runtests
from math import inf

def copy_tab(tab):
    new_tab = []
    for item in tab:
        new_tab.append(item)
    return new_tab

def iamlate(T, V, q, l):
    n = len(T)
    memo = [[[inf, []] for i in range(n)]for i in range(q + 1)]
    memo[0][0] = [0, []]
    for i in range(1, q + 1):
        if i <= V[0]:
            memo[i][0] = [1, [0]]

    for i in range(1, n):
        dist = T[i] - T[i - 1]
        for j in range(q + 1):
            if j + dist <= q:
                if memo[j+dist][i-1][0] <= memo[j][i][0]:
                    memo[j][i] = memo[j+dist][i-1]
                    amount = memo[j][i][0] + 1
                    tab = memo[j][i][1]
                    new_tab = copy_tab(tab)
                    new_tab.append(i)
                    for k in range(1, V[i] + 1):
                        if j + k <= q and amount < memo[j+k][i][0]:
                            memo[j + k][i] = [amount, new_tab]

    how_much = l - T[n - 1]
    if how_much >= 0 and how_much <= q and memo[how_much][n - 1][0] != inf:
        return memo[how_much][n - 1][1]

    return []

runtests( iamlate )
