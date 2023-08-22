from kol3atesty import runtests
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

def add_blackhole(graph, S):
    n = len(S)
    for i in range(n-1):
        graph[S[i]].append([S[i + 1], 0])
        graph[S[i + 1]].append([S[i], 0])


def find_max(E, S):
    maximum = 0
    n = len(E)
    for i in range(n):
        if E[i][0] > maximum:
            maximum = E[i][0]
        if E[i][1] > maximum:
            maximum = E[i][1]
    for k in range(len(S)):
        if S[k] > maximum:
            maximum = S[k]
    return maximum



def create_graph(E, S):
    n = len(E)
    length = find_max(E, S)
    new_graph = [[] for i in range(length + 1)]
    for i in range(n):
        curr1 = E[i][0]
        curr2 = E[i][1]
        cost = E[i][2]
        new_graph[curr1].append([curr2, cost])
        new_graph[curr2].append([curr1, cost])

    return new_graph

def spacetravel( n, E, S, a, b ):
    graph = create_graph(E, S)
    add_blackhole(graph, S)
    tab = Dijkstra(graph, a)

    if tab[b] == inf:
        return None
    return tab[b]


runtests( spacetravel, all_tests = True )