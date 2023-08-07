# Time Complexity : O(n^2)

tab = [9,2,5,1,3,7,12,5,11,4,2,2,7,9,10,0]
print(tab)

def InsertionSort(tab):
    n = len(tab)
    for i in range(n):
        j = i
        while j > 0 and tab[j]<tab[j-1]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j-=1

InsertionSort(tab)
print(tab)
