from zad1testy import runtests
import math

def reorder(tab):
    n = len(tab)
    for i in range(n):
        tab[i].append(i)

def convert_to_tuple(tab):
    new_tab = []
    n = len(tab)
    for i in range(n):
        tuple = [tab[i], i]
        new_tab.append(tuple)
    return new_tab

def Tuple_Merge(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        Tuple_Merge(L)
        Tuple_Merge(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i][0] <= P[j][0]:
                tab[k] = L[i]
                i += 1
                k += 1
            else:
                tab[k] = P[j]
                j += 1
                k += 1
        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1
        while j < len(P):
            tab[k] = P[j]
            j += 1
            k += 1


def chaos_index( T ):
    K = 0
    n = len(T)
    tab = convert_to_tuple(T)
    Tuple_Merge(tab)
    reorder(tab)

    for i in range(n):
        if K < abs(tab[i][2] - tab[i][1]):
            K = abs(tab[i][2] - tab[i][1])


    return K



runtests( chaos_index )
