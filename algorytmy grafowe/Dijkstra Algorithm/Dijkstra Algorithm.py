from math import inf
from queue import PriorityQueue

graph = [[(1, 1), (7, 2)], [(0, 1), (2, 3), (4, 3)], [(1, 3), (3, 5)], [(2, 5), (4, 2), (6, 1)], [(1, 3), (3, 2), (5, 3), (7, 1)], [(4, 3), (6, 8), (8,1)], [(5,8), (3, 1), (8, 4)], [(0, 2), (4, 1), (8, 7)], [(7, 7), (5, 1), (6, 4)] ]


def relax(G, s, node, neighbour_num, distance, parents, node_to_neigh, PriorQ ):
    if distance[neighbour_num] > distance[node] + node_to_neigh:
        distance[neighbour_num] = distance[node] + node_to_neigh
        parents[neighbour_num] = node
        PriorQ.put((distance[neighbour_num], neighbour_num))



def Dijkstra(G, s):
    parents = [None for i in range(len(G))]
    distance = [inf for j in range(len(G))]
    distance[s] = 0
    PriorQ = PriorityQueue()
    PriorQ.put((0, s))
    while PriorQ.qsize() > 0:
        curr = PriorQ.get()
        node = curr[1]
        for neighbour in (G[node]):
            node_to_neigh = neighbour[1]
            neighbour_num = neighbour[0]
            relax(G, s, node, neighbour_num, distance,parents,  node_to_neigh, PriorQ)
    return distance


a = Dijkstra(graph, 0)
print(a)


