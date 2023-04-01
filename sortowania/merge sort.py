tab = [3,1,7,5,6,10,15,7,13,9,3,6,7]
print(tab)
def Merge_Sort(tab):
    if len(tab)>1:
        mid=len(tab)//2
        L=tab[:mid]
        P=tab[mid:]
        Merge_Sort(L)
        Merge_Sort(P)

        i=j=k=0
        while i<len(L) and j<len(P):
            if L[i]<P[j]:
                tab[k]=L[i]
                i+=1
                k+=1
            else:
                tab[k]=P[j]
                j+=1
                k+=1
        while i<len(L):
            tab[k]=L[i]
            i+=1
            k+=1
        while j<len(P):
            tab[k]=P[j]
            j+=1
            k+=1

Merge_Sort(tab)
print(tab)