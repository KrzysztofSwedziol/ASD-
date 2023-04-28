#Krzysztof Swędzioł 418001
#Algorytm działa w następujący sposób : najpierw przepisuję z postaci krawędziowej grafu do postaci listowej wszystkie
#wierzchołki i krawędzie w celu ułatwienia sobie pracy a potem przepisuję do nowego grafu wszystkie wierzchołki z
#miejsca przy osobliwości połączone ze sobą i z wagą 0. Następnie realizuję algorytm Dijkstry i zwracam tablicę distance
#która ma zapisana w sobie najkrótsze odległości każdego z wierzchołków od wierzchołka startowego. Następnie odczytuję
#odległość dla zadanego wierzchołka i ją zwracam a w przypadku gdy jest ona nieskończona zwracam None.

from zad5testy import runtests
from math import inf
from queue import PriorityQueue

def relax(G, s, node, neighbour_num, distance, node_to_neigh, PriorQ ):
    if distance[neighbour_num] > distance[node] + node_to_neigh:
        distance[neighbour_num] = distance[node] + node_to_neigh
        PriorQ.put((distance[neighbour_num], neighbour_num))



def Dijkstra(G, s):
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
            relax(G, s, node, neighbour_num, distance, node_to_neigh, PriorQ)
    return distance

def spacetravel( n, E, S, a, b ):
    graph = [[] for i in range(n)]
    for j in E:
        node1 = j[0]
        node2 = j[1]
        time = j[2]
        graph[node1].append((node2, time))
        graph[node2].append((node1, time))
    for k in S:
        for l in S:
            if k != l :
                graph[k].append((l, 0))

    dist = Dijkstra(graph, a)
    if dist[b] != inf:
        return dist[b]

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )