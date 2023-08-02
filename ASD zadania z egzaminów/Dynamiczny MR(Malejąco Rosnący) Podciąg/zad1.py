from zad1testy import runtests

def copy_tab(tab1):
    n = len(tab1)
    start = 0
    end = n
    tab = tab1[start:end]
    return tab


def connect_tabs(tab1, tab2, tab3):
    n = len(tab1)
    z = len(tab2)
    for i in range(n):
        tab3.append(tab1[i])
    for l in range(z):
        tab3.append(tab2[l])

def copy_backwards(tab1, curr):
    n = len(tab1)
    start = 0
    end = n
    tab2 = []
    tab2.append(curr)
    tab3 = tab1[start:end]
    tab2.extend(tab3)
    return tab2


def mr( X ):
    n = len(X)
    memo_descending = [[0, []] for i in range(n)]
    memo_growing = [[0, []] for i in range(n)]
    memo_growing_backwards = [[0, []] for i in range(n)]

    for p in range(n):
        memo_descending[p][0] = 1
        memo_descending[p][1].append(X[p])

        memo_growing[p][0] = 1
        memo_growing[p][1].append(X[p])

    for h in range(n-1, -1, -1):
        memo_growing_backwards[h][0] = 1
        memo_growing_backwards[h][1].append(X[h])

    for i in range(1, n):
        curr = X[i]
        for j in range(i-1, -1, -1):
            if curr < X[j] and memo_descending[i][0] < memo_descending[j][0] + 1:
                memo_descending[i][0] =  memo_descending[j][0] + 1
                tab = copy_tab(memo_descending[j][1])
                tab.append(curr)
                memo_descending[i][1] = tab
    for k in range(1, n):
        curr = X[k]
        for z in range(k-1, -1, -1):
            if curr > X[z] and memo_growing[k][0] < memo_growing[z][0] + 1:
                memo_growing[k][0] = memo_growing[z][0] + 1
                tab2 = copy_tab(memo_growing[z][1])
                tab2.append(curr)
                memo_growing[k][1] = tab2

    for t in range(n-2, -1, -1):
        curr = X[t]
        for g in range(t + 1, n):
            if curr < X[g] and memo_growing_backwards[t][0] < memo_growing_backwards[g][0] + 1:
                memo_growing_backwards[t][0] = memo_growing_backwards[g][0] + 1
                tab3 = copy_backwards(memo_growing_backwards[g][1], curr)
                memo_growing_backwards[t][1] = tab3

    maximum = 0
    max_tab = None
    for y in range(n):
        option1 = memo_descending[y][0]
        tabb1 = memo_descending[y][1]
        option2 = memo_growing[y][0]
        tabb2 = memo_growing[y][1]
        if option1 > maximum:
            maximum = option1
            max_tab = tabb1
        if option2 > maximum :
            maximum = option2
            max_tab = tabb2

    for p in range(n):
        for o in range(p + 1, n):

            option = memo_descending[p][0] + memo_growing_backwards[o][0]
            if option >= maximum:
                maximum = option
                tabb = []
                connect_tabs(memo_descending[p][1], memo_growing_backwards[o][1], tabb)
                max_tab = tabb

    return max_tab

    
runtests( mr )


