#Krzysztof Swędzioł 418001
#Algorytm działa następująco : idziemy po tablicy i tą tablicę ograniczamy zakresem - iterujem po tablicy
#len(T) - p + 1 razy bo tyle razy rozważamy przedziały w tablicy, następnie za każdą iteracją używamy quick selecta (
#algorytm który dla zadanej tablicy i indexu zwraca liczbę która by się znalazła na tym indeksie w posortowanej tablicy)
#aby znaleźć k-ty największy element, czyli ten na pozycji k-p w zadanym przedziale, który potem dodajemy do sumy.
#Na koniec zwracamy sumę
#Algorytm działa w czasie O(np) - quick select dla zadanego przedziału działa w przybliżeniu w czasie liniowym a używamy
#go n razy.

from kol1testy import runtests

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




def ksum(T, k, p):
    n = len(T)
    iterator = len(T) - p + 1
    sum = 0
    iterator_v2 = 0
    curr_val = 0
    for i in range(iterator):
        curr_tab = T[iterator_v2 : iterator_v2 + p ]

        quick_select(curr_tab, 0, len(curr_tab) - 1, p - k)

        curr_val = curr_tab[p - k]

        sum += curr_val
        iterator_v2 +=1

    return sum

    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
