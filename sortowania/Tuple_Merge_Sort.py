tab = [(1,3), (7,2), (2,5), (3,6), (1,9), (9,5), (4,10)]

def Tuple_Merge(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        Tuple_Merge(L)
        Tuple_Merge(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i][0] < P[j][0]:
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

Tuple_Merge(tab)
print(tab)