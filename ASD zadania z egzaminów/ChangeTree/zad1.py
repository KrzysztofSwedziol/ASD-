from zad1testy import runtests
class Node:
  def __init__( self ):
    self.left    = None  # lewe podrzewo
    self.right   = None  # prawe poddrzewo
    self.parent  = None  # rodzic drzewa jesli istnieje
    self.value   = None  # przechowywana wartosc

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(tab, i, n):
    L=left(i)
    R=right(i)
    min_ind=i
    if L<n and tab[L]<tab[min_ind]:
        min_ind=L
    if R<n and tab[R]<tab[min_ind]:
        min_ind=R
    if min_ind!=i:
        tab[i], tab[min_ind]=tab[min_ind], tab[i]
        heapify(tab, min_ind, n)

def build_heap(tab):
    n=len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)

def travel(curr, tab):
    if curr != None:
        tab.append(curr.value)
        travel(curr.left, tab)
        travel(curr.right, tab)

def create_new(curr, index, tab, n):
    if index <= n-1:
        curr.val = tab[index]
        L = left(index)
        if L <= n-1:
            new_node_L = Node()
            curr.left = new_node_L
            create_new(new_node_L, L, tab, n)
        R = right(index)
        if R <= n-1:
            new_node_R = Node()
            curr.right = new_node_R
            create_new(new_node_R, R, tab, n)

def print_tree(curr):
    if curr != None:
        print(curr.val)
        print_tree(curr.left)
        print_tree(curr.right)


def ConvertTree(T):
    tab = []
    travel(T, tab)
    build_heap(tab)
    new_tree = Node()
    n = len(tab)
    create_new(new_tree, 0, tab, n)
    T = new_tree
    return T


runtests( ConvertTree )