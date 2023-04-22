#Krzysztof Swędzioł 418001
#Algorytm działa następująco : puszczamy BFS i znajdujemy najkrótszy dystans z s do t i go zapisujemy w zmiennej shortest_distance
#Następnie przechodzimy po krawędziach w najkrótszej ścieżce od tyłu i za każdym razem sprawdzamy BFS czy usunięcie
#danej krawędzi spowodowało wydłużenie się ścieżki, jeśli tak to zwracamy tą krawędź, jeśli nie, odkładamy tą krawędź
#do grafu i próbujemy z kolejną i tak aż do momentu aż dojdziemy z t do s i jeśli to się stanie i nie znaleźliśmy
#żądanej krawędzi to zwracamy None.
#Algorytm ma złożoność O(V(V + E)) - BFS ma złożoność O(V + E) i w najgorszym przypadku wykonujemy go V razy

from zad4testy import runtests
from collections import deque

def BFS(graph, starting_node, visited, parents, distance, t):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
        distance[v] = -1
    queue = deque()
    queue.append(starting_node)
    visited[starting_node] = True

    while (len(queue) > 0):
        current_node = queue.popleft()
        if current_node == t:
            break

        for neighbour in graph[current_node]:

            if visited[neighbour] == False:
                queue.append(neighbour)
                parents[neighbour] = current_node
                distance[neighbour] = distance[current_node] + 1
                visited[neighbour] = True


def longer( G, s, t ):
    visited = [False for i in range(len(G))]
    parents = [None for j in range(len(G))]
    distance = [-1 for k in range(len(G))]
    BFS(G, s, visited, parents, distance, t)
    shortest_distance = distance[t]
    if shortest_distance == -1:
        return None
    current_node = t
    current_node_parent = parents[current_node]
    deleted_node = []
    while current_node != s:
        G[current_node_parent].remove(current_node)
        G[current_node].remove(current_node_parent)
        BFS(G, s, visited, parents, distance, t)
        if distance[t] > shortest_distance or distance[t] == -1:
            return (current_node_parent, current_node)
        else:
            G[current_node_parent].append(current_node)
            G[current_node].append(current_node_parent)

            current_node = current_node_parent
            current_node_parent = parents[current_node_parent]

    return None



    return (0,0)




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )