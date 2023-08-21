from kolutesty import runtests

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


def ice_cream( T ):
    n = len(T)
    BucketSort(T)
    counter = 0
    sum = 0
    for i in range(n-1, -1, -1):
        if T[i] - counter > 0:
            sum += T[i] - counter
            counter += 1
        else :
            break
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
