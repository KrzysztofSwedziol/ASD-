#Kolejka Priorytetowa z kopcem maximum - im większa wartość tym wyższy priorytet

def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(l):
    return (l-1)//2

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

class priority_queue():
    def __init__(self):
        self.tab = []
    def size(self):
        return len(self.tab)
    def is_empty(self):
        if len(self.tab)==0 :
            return True
        return False
    def push(self, item):
        self.tab.append(item)
        self.tab[0], self.tab[len(self.tab)-1]=self.tab[len(self.tab)-1], self.tab[0]
        heapify(self.tab, 0, len(self.tab))
    def pop(self):
        a = self.tab[0]
        self.tab[0]=self.tab[len(self.tab)-1]
        del self.tab[len(self.tab)-1]

    def top(self):
        return self.tab[0]


z = priority_queue()
z.push(5)
z.push(3)
z.push(9)
print(z.top())
print(z.size())
print(z.is_empty())
z.pop()
print(z.top())
print(z.size())

