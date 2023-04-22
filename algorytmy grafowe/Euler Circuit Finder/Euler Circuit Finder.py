
graph = [[1,2], [0, 6, 3, 4, 2, 5], [1, 0, 6, 3, 4, 5], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4], [1,2] ]



def Euler_Circuit_Finder(G):
    visited_edges = []
    Euler = []
    DFS(G, visited_edges, Euler)

    return Euler




def explore(graph, node, visited_edges, Euler):
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    for neighbour in graph[node]:
       if (neighbour, node) not in visited_edges and (node, neighbour) not in visited_edges:
            visited_edges.append((neighbour, node))
            visited_edges.append((node, neighbour))
            explore(graph, neighbour, visited_edges, Euler)
    time +=1   #wierzchołek został przetworzony i time to czas przetworzenia
    Euler.append(node)


def DFS(graph, visited_edges, Euler):
    global time
    time = 0
    v = 0
    explore(graph, v, visited_edges, Euler)


a = Euler_Circuit_Finder(graph)
print(a)