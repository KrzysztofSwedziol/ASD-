def Tuple_Merge(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        Tuple_Merge(L)
        Tuple_Merge(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i][2] < P[j][2]:
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


def Tuple_Merge2(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        Tuple_Merge2(L)
        Tuple_Merge2(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i][1] >= P[j][1]:
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




def count(number):
    tab = [0 for i in range(10)]
    while number > 0:
        curr_num = number%10
        tab[curr_num] += 1
        number=number//10
    single = 0
    multi = 0
    for i in range(10):
        if tab[i] > 1:
            multi += 1
        if tab[i] == 1:
            single += 1

    return single, multi



def convert_tab(tab):
    n = len(tab)
    new_tab = [[] for i in range(n)]
    for i in range(n):
        curr = tab[i]
        single, multi = count(curr)
        new_tab[i] = [curr, single, multi]
    return new_tab



def pretty_sort(T):
    n = len(T)
    new_tab = convert_tab(T)
    Tuple_Merge(new_tab)
    Tuple_Merge2(new_tab)

    for i in range(n):
        T[i] = new_tab[i][0]


T = [123, 455, 1266, 114577, 2344, 6733]
pretty_sort(T)
print(T)

