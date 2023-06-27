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