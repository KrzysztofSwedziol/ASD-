from egz1Atesty import runtests

from math import inf
from queue import PriorityQueue
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

def Change_Graph(graph, r):
    n = len(graph)
    for i in range(n):
        for j in range(len(graph[i])):
            graph[i][j][1] = graph[i][j][1]*2 + r

def tuple_to_table(graph):
    n= len(graph)
    new_graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(graph[i])):
            new_graph[i].append([graph[i][j][0], graph[i][j][1]])

    return new_graph


def gold(G,V,s,t,r):
    n = len(G)
    G = tuple_to_table(G)
    tab = [inf for i in range(n)]
    dist1 = Dijkstra(G, s)
    Change_Graph(G, r)
    dist2 = Dijkstra(G, t)
    for i in range(n):
        tab[i] = dist1[i] + dist2[i] - V[i]
    minimum = min(tab)
    return minimum
    pass


runtests( gold, all_tests = True )
