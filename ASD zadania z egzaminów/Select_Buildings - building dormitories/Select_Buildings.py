def copy_tab(tab1, tab2):
    n = len(tab1)
    for i in range(n):
        tab2.append(tab1[i])


def select_buildings(T, p):
    n = len(T)

    new_tab = [[] for i in range(n)]
    cost = [0] * n
    parent = [None] * n
    students = [0] * n

    for i in range(n):
        height = T[i][0]
        a = T[i][1]
        b = T[i][2]
        cost1 = T[i][3]
        new_tab[i].append(height)
        new_tab[i].append(a)
        new_tab[i].append(b)
        new_tab[i].append(cost1)
        new_tab[i].append(i)


    new_tab.sort(key = lambda x : x[2])

    for i in range(n):
        cost[i] = new_tab[i][3]
        students[i] = (new_tab[i][2] - new_tab[i][1]) * new_tab[i][0]
        for j in range(i-1, -1, -1):
            if new_tab[j][2] < new_tab[i][1]:
                parent[i] = j
                break

    memo = [[[0, []] for i in range(n)] for j in range(p + 1)]

    for i in range(p + 1):
        curr_cost = new_tab[0][3]
        if i >= curr_cost:
            students2 = (new_tab[0][2] - new_tab[0][1]) * new_tab[0][0]
            memo[i][0][0] = students2
            memo[i][0][1].append(new_tab[0][4])


    for i in range(1, n):
        for j in range(1, p + 1):
            memo[j][i][0] = memo[j][i-1][0]
            curr_tab = memo[j][i-1][1]
            new_table = []
            copy_tab(curr_tab, new_table)
            memo[j][i][1] = new_table

            curr_cost = new_tab[i][3]
            if parent[i] is not None and cost[i] < j:
                if memo[j][i][0] < memo[j-curr_cost][parent[i]][0] + students[i]:
                    memo[j][i][0] = memo[j-curr_cost][parent[i]][0] + students[i]
                    new_table.append(new_tab[i][4])
                    memo[j][i][1] = new_table
            elif parent[i] is None and cost[i] < j:
                if students[i] > memo[j][i][0]:
                    memo[j][i][0] = students[i]
                    tabb = []
                    tabb.append(new_tab[i][4])

    max_students = memo[p][n-1][0]
    tab_to_return = None
    for i in range(p-1, -1, -1):
        if memo[i][n-1][0] == max_students:
            tab_to_return = memo[i][n-1][1]
        if memo[i][n-1][0] < max_students:
            break

    return tab_to_return

T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]

p = 5

print(select_buildings(T, p))


    