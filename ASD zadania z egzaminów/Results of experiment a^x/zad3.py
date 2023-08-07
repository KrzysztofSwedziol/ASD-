from zad3testy import runtests
import math

def InsertionSort(tab):
    n = len(tab)
    for i in range(n):
        j = i
        while j > 0 and tab[j]<tab[j-1]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j-=1

    return tab



def BucketSort(tab):
    if len(tab) == 0:
        return tab

    min_val = min(tab)
    max_val = max(tab)
    range_val = max_val - min_val
    slots = len(tab)
    buckets = [[] for i in range(slots)]

    for j in tab:
        index = int((slots - 1) * (j - min_val) / range_val)
        buckets[index].append(j)

    for i in range(slots):
        buckets[i] = InsertionSort(buckets[i])

    k = 0
    for i in range(slots):
        for j in range(len(buckets[i])):
            tab[k] = buckets[i][j]
            k += 1

    return tab


                 
    
def fast_sort(tab, a):
    BucketSort(tab)
    return tab



runtests( fast_sort )
