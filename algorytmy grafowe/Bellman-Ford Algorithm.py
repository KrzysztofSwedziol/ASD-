from math import inf
graph = [[(1, 1), (7, 2)], [(0, 1), (2, 3), (4, 3)], [(1, 3), (3, 5)], [(2, 5), (4, 2), (6, 1)], [(1, 3), (3, 2), (5, 3), (7, 1)], [(4, 3), (6, 8), (8,1)], [(5,8), (3, 1), (8, 4)], [(0, 2), (4, 1), (8, 7)], [(7, 7), (5, 1), (6, 4)] ]

def verify(G, S, distance, parent):
    for v in range(len(G)):
        for neighbour in G[v]:
            if distance[v] > distance[neighbour[0]] + neighbour[1]:
                return False
    return True

def Relax(G, S, distance, parent):
    for i in range(len(G) - 1):
        for v in range(len(G)):
            for neighbour in G[v]:
                if distance[neighbour[0]] > distance[v] + neighbour[1]:
                    distance[neighbour[0]] = distance[v] + neighbour[1]
                    parent[neighbour[0]] = v

def Bellman_Ford(G, S):
    parent = [None for i in range(len(G))]
    distance = [inf for j in range(len(G))]
    distance[S] = 0

    Relax(G, S, distance, parent)

    a = verify(G, S, distance, parent)
    if a == False:
        return None
    else:
        return distance

print(Bellman_Ford(graph, 0))



