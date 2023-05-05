from queue import PriorityQueue
from math import inf

graph = [[(1, 1), (4, 5), (5, 8)], [(0, 1), (2, 3)], [(1, 3), (3, 6), (4, 4)], [(2, 6), (4, 2)], [(0, 5), (2, 4), (3, 2), (5, 7)], [(0, 8), (4, 7)]]

def Relax(G, curr, neighbour, parent, edge_weight, prior):
    neighbour_num = neighbour[0]
    neighbour_weight = neighbour[1]
    if edge_weight[neighbour_num] > neighbour_weight and parent[curr] != neighbour_num:
        edge_weight[neighbour_num] = neighbour_weight
        parent[neighbour_num] = curr
        prior.put((neighbour_weight, neighbour_num))


def Prim(G, S):
    n = len(G)
    parent = [None for i in range(n)]
    prior = PriorityQueue()
    prior.put((0, S))
    edge_weight = [inf for i in range(n)]
    edge_weight[S] = 0
    while prior.qsize() > 0:
        curr = prior.get()
        curr = curr[1]
        for neighbour in G[curr]:
            Relax(G, curr, neighbour, parent, edge_weight, prior)

    for vertex in range(n):
        print("curr vertex :", vertex)
        print("edge weight : ", edge_weight[vertex])
        print("curr vert parent : ", parent[vertex])


Prim(graph, 0)

