from zad3testy import runtests
from math import inf
from queue import PriorityQueue
from collections import deque
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
    return distance, parents



def paths(G, s, t):
    n = len(G)
    dist, par = Dijkstra(G, s)
    dist2, par2 = Dijkstra(G, t)

    if dist[t] == inf:
        return 0

    counter = 0
    for u in range(n):
        for v, w in G[u]:
            if dist[u] + w + dist2[v] == dist[t]:
                counter += 1
    return counter  
    
runtests( paths )


