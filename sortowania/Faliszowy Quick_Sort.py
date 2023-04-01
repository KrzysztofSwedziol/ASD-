tab = [1,6,8,4,7,9,2,4,5,7,8,5,7]
print(tab)

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

quick_sort(tab, 0, len(tab)-1)
print(tab)