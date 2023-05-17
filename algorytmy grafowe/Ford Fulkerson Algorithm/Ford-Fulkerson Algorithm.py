#Algorithm for finding maximum flow in graph

from collections import deque

graph = [[0 for j in range(6)] for i in range(6)]
graph[0][1] = 4
graph[0][3] = 3
graph[1][2] = 2
graph[1][3] = 2
graph[2][5] = 4
graph[3][2] = 2
graph[3][4] = 2
graph[4][5] = 5

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

a = Ford_Fulkerson(graph, 0, len(graph)-1)
print(a)




