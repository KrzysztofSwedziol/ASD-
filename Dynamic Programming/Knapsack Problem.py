#first value is weight, second value is cost of an item
items = [(5,3), (7,9), (2,3), (5,5), (9,13), (10, 10), (1,1), (4, 8), (6, 9), (15, 420), (25, 2137)]


def Knapsack(items, weight):
    n = len(items)
    result_tab = [[0 for i in range(weight+1)] for j in range(n)]
    for i in range(weight+1):
        if items[0][0] <= i:
            result_tab[0][i] = items[0][1]
    for i in range(1, n):
        for b in range(weight+1):
            if b - items[i][0] >= 0:
                result_tab[i][b] = max(result_tab[i-1][b], result_tab[i-1][b-items[i][0]] + items[i][1])

            else :
                result_tab[i][b] = result_tab[i-1][b]


    return result_tab[n-1][weight]

print(Knapsack(items, 30))
    

