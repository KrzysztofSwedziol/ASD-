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


def BFS(G, starting_node):
    queue = deque()
    queue.append(starting_node)
    while len(queue)>0:
        curr_node = queue.popleft()
        curr_node.visited = True

        print("current node : ", curr_node.name)
        print("current node's distance from start : ", curr_node.distance)
        print("current node's parent : ", curr_node.parent)
        
        for neighbour in G.graph[curr_node]:
            if neighbour.visited == False :
                queue.append(neighbour)
                neighbour.visited = True
                neighbour.distance = curr_node.distance + 1
                neighbour.parent = curr_node.name

BFS(G, A)




