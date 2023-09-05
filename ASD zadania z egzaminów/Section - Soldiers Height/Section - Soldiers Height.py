def partition(tab, start, end):
    pivot = tab[end]
    i = start - 1
    for j in range(start, end):
        if (tab[j]< pivot):
            tab[i+1], tab[j]=tab[j],tab[i+1]
            i +=1
    tab[i+1], tab[end]=tab[end], tab[i+1]
    return i+1

def quick_select(tab, start, end, k):
    a = partition(tab, start, end )

    if a > k:
        quick_select(tab, start, a-1, k )
    if a < k:
        quick_select(tab, a+1, end, k)

def Section(T, p, q):
    quick_select(T, 0, len(T) - 1, p)
    quick_select(T, 0, len(T) - 1, q)

    return T[p:q+1]


T = [1,2,5,8,5,4,3,2,7,9,0,8,7,6,9,0,4,6,5,4,3]
T2 = [1,2,5,8,5,4,3,2,7,9,0,8,7,6,9,0,4,6,5,4,3]
T2.sort()
print(T2)
print(Section(T, 5, 8))