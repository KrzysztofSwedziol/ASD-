#we get table of tuples that represent time period and our task is to pick as much as we can without conflicts
tab = [(1,3), (5,7), (9,10), (2,4), (1,5), (3,9), (3,6), (5,8), (11, 15), (12, 17)]

def Optimal_Select(tab):
    n = len(tab)
    result_tab = []
    new_tab = tab
    new_tab.sort(key = lambda x : x[1])
    loaded = [0,0]
    for i in range(n):
        curr = new_tab[i]
        if curr[0] < loaded[1] and curr[0] > loaded[0] or curr[1] > loaded[0] and curr[1] < loaded[1]:
            continue
        else:
            result_tab.append(curr)
            loaded = [0,curr[1]]

    return result_tab

print(Optimal_Select(tab))

