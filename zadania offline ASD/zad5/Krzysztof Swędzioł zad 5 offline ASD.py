#Krzysztof Swędzioł 418001
#Algorytm działa w następujący sposób : najpierw przepisuję z postaci krawędziowej grafu do postaci listowej wszystkie
#wierzchołki i krawędzie w celu ułatwienia sobie pracy i dodaję do grafu nowy wierzchołek
#stanowiący przejście pomiędzy wierzchołkami koło osobliwości i nadaję krawędziom do tego wierzchołka wagę 0.
#Następnie realizuję algorytm Dijkstry i zwracam tablicę distance wtedy gdy z kolejki zdjęty został szukany wierchołek
#bo to oznacza że znaleźliśmy szukany dystans.
#Następnie odczytuję odległość dla zadanego wierzchołka i ją zwracam a w przypadku gdy jest ona nieskończona zwracam None.
#Algorytm działa w czasie O(ElogV)

from zad5testy import runtests
from math import inf
from queue import PriorityQueue

def relax(G, s, node, neighbour_num, distance, node_to_neigh, PriorQ ):
    if distance[neighbour_num] > distance[node] + node_to_neigh:
        distance[neighbour_num] = distance[node] + node_to_neigh
        PriorQ.put((distance[neighbour_num], neighbour_num))



def Dijkstra(G, s, b):
    distance = [inf for j in range(len(G))]
    distance[s] = 0
    PriorQ = PriorityQueue()
    PriorQ.put((0, s))
    while PriorQ.qsize() > 0:
        curr = PriorQ.get()
        node = curr[1]
        if node == b:
            break
        for neighbour in (G[node]):
            node_to_neigh = neighbour[1]
            neighbour_num = neighbour[0]
            relax(G, s, node, neighbour_num, distance, node_to_neigh, PriorQ)
    return distance

def spacetravel( n, E, S, a, b ):
    graph = [[] for i in range(n+1)]
    for j in E:
        node1 = j[0]
        node2 = j[1]
        time = j[2]
        graph[node1].append((node2, time))
        graph[node2].append((node1, time))
    for x in S:
        graph[n].append((x, 0))
        graph[x].append((n, 0))

    dist = Dijkstra(graph, a, b)
    if dist[b] != inf:
        return dist[b]

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )