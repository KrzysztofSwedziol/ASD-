from zad3testy import runtests

def find_proper(tab, T, new_tab, visited):
    most_prev = 0
    n = len(tab)
    for k in tab:
        if visited[k] == False:
            most_prev = k
            break
    for i in tab:
        if T[most_prev][i] == 2 and visited[i] == False:
            most_prev = i
    visited[most_prev] = True
    return most_prev


def tasks(T):
    n = len(T)
    tab = [[] for i in range(n)]

    for i in range(n):
        before = 0
        after = 0
        mid = 0
        for j in range(n):
            if T[i][j] == 1:
                after += 1
            if T[i][j] == 2:
                before += 1
            if T[i][j] == 0:
                mid += 1
        if mid == 1:
            tab[before].append(i)
        if mid > 1:
            while mid >= 1:
                tab[before + mid - 1].append(i)
                mid -= 1

    new_tab = [None for i in range(n)]
    used = [False for i in range(n)]
    
    for i in range(n):
        new_tab[i] = find_proper(tab[i], T, new_tab, used)

    return new_tab

runtests( tasks )
