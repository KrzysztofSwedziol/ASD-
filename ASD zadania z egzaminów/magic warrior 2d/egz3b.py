from egz3btesty import runtests
from math import inf


def copy_table(memo, memo_copy, curr_col, prev_col, n):
    for i in range(n):
        memo_copy[i][curr_col] = memo[i][curr_col]
        memo_copy[i][prev_col] = memo[i][prev_col]

def select_option(memo, memo_copy, column, n):
    for i in range(n):
        if memo_copy[i][column] > memo[i][column]:
            memo[i][column] = memo_copy[i][column]



def select_best(L, tab, row, column, n):
    if L[row][column] == "#":
        tab[row][column] = -inf
    else:
        best = -inf
        if column - 1 >= 0 and L[row][column-1] != "#":
            if tab[row][column-1] + 1 > best:
                best = tab[row][column-1] + 1
        if row - 1 >=0 and L[row - 1][column] != "#":
            if tab[row - 1][column] + 1 > best:
                best = tab[row - 1][column] + 1
        if row + 1 <= n-1 and L[row + 1][column] != "#":
            if tab[row + 1][column] + 1 > best:
                best = tab[row + 1][column] + 1
        if best > tab[row][column] :
            tab[row][column] = best


def maze( L ):
    n = len(L)
    memo = [[-inf for i in range(n)] for j in range(n)]
    memo[0][0] = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] == "#":
                memo[i][j] = -inf

    #set first column
    flag = True
    for k in range(1, n):
        if L[k][0] != "#"  and flag == True:
            memo[k][0] = memo[k-1][0] + 1
        if L[k][0] == "#":
            flag = False
        if flag == False:
            memo[k][0] = -inf


    for i in range(1, n):
        memo_copy = [[-inf for i in range(n)] for j in range(n)]
        copy_table(memo, memo_copy, i, i-1, n)
        for j in range(n):
            select_best(L, memo, j, i, n)
        for k in range(n-1, -1, -1):
            select_best(L, memo_copy, k, i, n)
        select_option(memo, memo_copy, i, n)

    if memo[n-1][n-1] == -inf:
        return -1
    return memo[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
