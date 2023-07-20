from egz2btesty import runtests

def magic( C ):
    n = len(C)
    result_tab = [-1 for i in range(n)]
    result_tab[0] = 0
    max_gold = 0
    for i in range(1, n):
        for j in range(i -1 , -1, -1):
            for k in range(1, 4):
                if C[j][k][1] == i :
                    max_gold = -1
                    if C[j][0] >= C[j][k][0] and C[j][0] - C[j][k][0] <=10:
                        max_gold = result_tab[j] + C[j][0] - C[j][k][0]
                    if C[j][0] < C[j][k][0] and C[j][k][0] - C[j][0] <= result_tab[j]:
                        max_gold = result_tab[j] - (C[j][k][0] - C[j][0])
                    if max_gold > result_tab[i]:
                        result_tab[i] = max_gold


    return result_tab[n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True  )
