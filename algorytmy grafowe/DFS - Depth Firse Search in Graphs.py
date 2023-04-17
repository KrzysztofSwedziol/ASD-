# A-----------C\
# |           |  \
# |           |    \
# |           |     E
# |           |    /
# |           |  /
# B-----------D/

from collections import deque

class Node:
    def __init__(self, Name):
        self.visited = False
        self.parent = None
        self.name = Name
        self.distance = 0



class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.graph = {}

        for node in self.nodes :
            self.graph[node] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def print_graph(self):
        for node in self.nodes:
            print(node.name, "--->", self.graph[node])

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")


Nodes = [A, B, C, D, E]

G = Graph(Nodes)
G.add_edge(A, B)
G.add_edge(A, C)
G.add_edge(B, D)
G.add_edge(C, D)
G.add_edge(C, E)
G.add_edge(D, E)

def Explore_Node(G,parent, Node, stack):
    Node.visited = True
    Node.parent = parent

    print("current node : ", Node.name)
    print("current node's parent : ", Node.parent.name)

    for neighbour in G.graph[Node]:
        if neighbour.visited == False:
            Explore_Node(G,Node, neighbour, stack)




def DFS(G, starting_node):
    stack = deque()
    start = starting_node
    start.visited = True
    stack.append(start)

    print("current node : ", start.name)
    print("current node's parent : ", start.parent)

    for neighbour in G.graph[start]:
        if neighbour.visited == False:
            Explore_Node(G, start, neighbour, stack)

DFS(G, A)


