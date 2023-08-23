def partition(tab, start, end):
    pivot = tab[end]
    i = start - 1
    for j in range(start, end):
        if (tab[j]< pivot):
            tab[i+1], tab[j]=tab[j],tab[i+1]
            i +=1
    tab[i+1], tab[end]=tab[end], tab[i+1]
    return i+1

def quick_sort(tab, start, end):
    if(start<end):
        pivot = partition(tab, start, end)
        quick_sort(tab, start, pivot-1)
        quick_sort(tab, pivot+1, end)

def convert_tab(T, tab):
    n = len(T)
    for i in range(n):
        for j in range(n):
            tab.append(T[i][j])



def Median(T):
    n = len(T)
    tab = []
    convert_tab(T, tab)
    quick_sort(tab, 0, len(tab)-1)
    new_tab = [[0 for i in range(n)]for i in range(n)]
    counter = len(tab) - 1
    for i in range(n):
        for j in range(n-1, -1, -1):
            new_tab[i][j] = tab[counter]
            counter -= 1

    return new_tab


T = [ [ 2, 3, 5],
    [ 7,11,13],
    [17,19,23] ]

new_tab = Median(T)
for i in range(len(T)):
    print(new_tab[i])