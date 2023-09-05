from collections import deque
from math import inf

def Floyd_Warshall(G):
    n = len(G)
    distance = [[inf for i in range(n)] for j in range(n)]
    parent = [[None for i in range(n)] for j in range(n)]

    for p in range(n):
        for u in range(n):
            if G[p][u] == 0:
                distance[p][u] = inf
            else:
                distance[p][u] = G[p][u]
        distance[p][p] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                    parent[i][j] = parent[k][j]


    for i in range(n):

        if distance[i][i] < 0:
            return False

    return distance, parent

def Ford_Fulkerson(g, source, sink):
    graph = g
    Max_Flow = 0
    parent = [-1]*len(graph)
    while BFS(graph, source, sink, parent):
        v = sink
        path_flow = float('inf')
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = parent[v]
        Max_Flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return Max_Flow



def BFS(graph, source, sink, parent):
    visited = [False for i in range(len(graph))]
    queue = deque()
    queue.append(source)
    visited[source] = True
    while len(queue) > 0:
        curr = queue.popleft()
        for neighbour in range(len(graph)):
            if visited[neighbour] == False and graph[curr][neighbour] > 0:
                visited[neighbour] = True
                parent[neighbour] = curr
                queue.append(neighbour)

    return visited[sink]

def create_graph(dist, K, D, new_graph):
    n = len(dist)
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= D and ((K[i] == "B" and K[j] == "G") or (K[j] == "G" and K[i] == "B")):
                new_graph[i+1][j+1] = 1
    for i in range(n):
        if K[i] == "B":
            new_graph[0][i+1] = 1
            new_graph[i+1][0] = 1
        if K[i] == "G":
            new_graph[n+1][i+1] = 1
            new_graph[i+1][n+1] = 1

def BlueAndGreen(T, K, D):
    n = len(T)
    new_graph = [[0 for i in range(n+2)] for j in range(n+2)]
    dist, parents = Floyd_Warshall(T)
    create_graph(dist, K, D, new_graph)
    flow = Ford_Fulkerson(new_graph, 0, n+1)
    return flow

T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ["B", "B", "G", "G", "B"]
D = 2

print(BlueAndGreen(T, K, D))