tab = [1,2,7,5,9,3,4,11,6]
print(tab)

def podziel(tab, start, end):
    low = start
    high = end - 1
    pivot = tab[end]
    while True:
        while low <= high and tab[low] <= pivot:
            low += 1
        while high >= low and tab[high] >= pivot:
            high -= 1
        if low <= high:
            tab[low], tab[high] = tab[high], tab[low]
        else:
            break

    tab[low], tab[end] = tab[end], tab[low]

    return low

def quick_sort(tab, start, end):
    if start < end:
        pivot = podziel(tab, start, end)
        quick_sort(tab, start, pivot - 1)
        quick_sort(tab, pivot + 1, end)

quick_sort(tab, 0, len(tab)-1)
print(tab)






