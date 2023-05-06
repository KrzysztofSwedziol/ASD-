# A-----------C\
# |           |  \
# |           |    \
# |           |     E
# |           |    /
# |           |  /
# B-----------D/

#-------------------------List Graph with parameters without dictionaries-----------------------------------------------

#A--->0, B--->1, C--->2, D--->3, E--->4

graph_prime = [[1,2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]]
visited_prime = [False for i in range(5)]
parents_prime = [[] for j in range(5)]

for x in range(5):
    print(x, '--->', graph_prime[x])

#-------------------------------------List Graph with Parameters--------------------------------------------------------
graph1 = {"A": ["B", "C"],
         "B": ["A", "D"],
         "C": ["A", "D", "E"],
         "D": ["B", "C", "E"],
         "E": ["C", "D"]}

visited = {"A": False, "B": False, "C": False, "D": False, "E": False}
parents = {"A": [], "B": [], "C": [], "D": [], "E": []}

print(graph1)

#--------------------------------------------Class Graph----------------------------------------------------------------
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
        self.parent = None
        self.name = Name




class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.graph = {}

        for node in self.nodes :
            self.graph[node] = []

    def add_edge(self, u, v, edge_weight):
        self.graph[u].append((v, edge_weight))
        self.graph[v].append((u, edge_weight))

    def print_graph(self):
        for node in self.nodes:
            for v in self.graph[node]:
                print(node.name, "--->", v[0].name, " weight : ", v[1])

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

G.print_graph()
#--------------------------------------------List Graph-----------------------------------------------------------------

graph = {"A": ["B", "C"],
         "B": ["A", "D"],
         "C": ["A", "D", "E"],
         "D": ["B", "C", "E"],
         "E": ["C", "D"]}

print(graph)

#---------------------------------------------Matrix Graph--------------------------------------------------------------

n = 5
Matrix_Graph = [[False for j in range(n)] for i in range(n)]

for l in range(n):
    for k in range(n):
        u = chr(ord('@') + l+1)
        g = chr(ord('@') + k+1)
        if g in graph[u]:
            Matrix_Graph[l][k]=True



for z in range(n):
    print(Matrix_Graph[z])
