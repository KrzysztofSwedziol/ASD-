tab=[3,1,7,5,6,10,15,7,13,9,3,6,7]
print(tab)
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(tab, i, n):
    L=left(i)
    R=right(i)
    max_ind=i
    if L<n and tab[L]>tab[max_ind]:
        max_ind=L
    if R<n and tab[R]>tab[max_ind]:
        max_ind=R
    if max_ind!=i:
        tab[i], tab[max_ind]=tab[max_ind], tab[i]
        heapify(tab, max_ind, n)

def build_heap(tab):
    n=len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)

def heapsort(tab):
    n=len(tab)
    build_heap(tab)
    for i in range(n-1, 0, -1):
        tab[i], tab[0]=tab[0], tab[i]
        heapify(tab, 0, i)

heapsort(tab)
print(tab)

