#we get table of fluids with its wights and its worth in tuples. Our task is to take te highest cost of them
tab = [(1,3), (4,7), (1,1), (7,4), (8,16), (15,10), (3,9), (4,20), (6,9), (9,9), (10, 20)]

def continous_knasack(tab, weight):
    n = len(tab)
    max_cost = 0
    new_tab = [[] for i in range(n)]
    for i in range(n):
        new_tab[i].append(tab[i][0])
        new_tab[i].append(tab[i][1])
        new_tab[i].append(tab[i][1]/tab[i][0])
    new_tab.sort(key = lambda x : x[2])
    new_tab.reverse()
    print(new_tab)
    for i in range(n):
        while weight > 0 and new_tab[i][0] > 0 :
            max_cost += new_tab[i][2]
            weight -= 1
            new_tab[i][0] -= 1
    return max_cost


print(continous_knasack(tab, 10))


