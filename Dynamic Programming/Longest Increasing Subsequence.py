#function gets table of numbers and returns table of longest increasing subsequence
tab = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]

def LIS(tab):
    result = []
    n = len(tab)
    result_tab = [[] for i in range(n)]
    result_tab[0] = [tab[0]]
    for i in range(1, n):
        for j in range(i, 0, -1):
            if tab[i] > tab[j-1] and len(result_tab[j-1]) + 1 > len(result_tab[i]) :
                result_tab[i] = result_tab[j-1] + [tab[i]]

    for i in range(n):
        if len(result_tab[i]) > len(result):
            result = result_tab[i]

    return result

print(LIS(tab))


