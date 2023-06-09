#Works on edge graph representation
from math import inf

# A-----5------C\
# |           |  6
# |           |    \
# 8           2     E
# |           |    /
# |           |  9
# B-----3------D/

class Node:
    def __init__(self, Name):
        self.visited = False
        self.parent = self
        self.name = Name
        self.rank = 0




class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.graph = []

    def add_edge(self, u, v, edge_weight):
        self.graph.append((v, u, edge_weight))

    def print_graph(self):
        for v in self.graph:
            print(v[0].name, v[1].name, v[2])


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
Nodes = [A, B, C, D, E]

G = Graph(Nodes)
G.add_edge(A, B, 8)
G.add_edge(A, C, 5)
G.add_edge(B, D, 3)
G.add_edge(C, D, 2)
G.add_edge(C, E, 6)
G.add_edge(D, E, 9)


def findset(node):
    if node.parent != node:
        node.parent = findset(node.parent)

    return node.parent



def union(set1, set2):
    set1 = findset(set1)
    set2 = findset(set2)
    if set1.rank > set2.rank:
        set2.parent = set1
        return set1

    else :
        set1.parent = set2
        if set1.rank == set2.rank:
            set2.rank+=1
        return set2



def Kruskal(graph):
    n = len(graph.graph)
    edges = graph.graph
    MST = []
    edges.sort(key = lambda x : x[2])

    for u, v, c in edges:
        x = findset(u)
        y = findset(v)
        if y != x:
            MST.append((u.name, v.name, c))
            union(x, y)
            if len(MST) == n - 1:
                break
    return MST

a = Kruskal(G)
print(a)


