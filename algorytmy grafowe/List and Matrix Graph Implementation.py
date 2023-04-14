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

    def add_edge(self, u, v):
        self.graph[u].append(v.name)
        self.graph[v].append(u.name)

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
