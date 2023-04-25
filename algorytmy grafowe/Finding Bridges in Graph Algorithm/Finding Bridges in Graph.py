from math import inf

Graph = [[1, 6], [0,2], [1, 6, 3], [2, 4, 5], [3, 5], [3, 4], [0, 2, 7], [6]]

def Find_Bridges(G):
    bridges = []
    visit_time = [0 for l in range(len(G))]
    visited = [False for i in range(len(G))]
    parents = [None for j in range(len(G))]
    time = 0
    low = [inf for i in range(len(G))]
    DFS(G, visited, parents, visit_time, low, bridges)
    return bridges



def explore(graph, node, visited, parents, visit_time, low, bridges):
    global time
    time += 1  # wierzchołek został odwiedzony i time to czas odwiedzenia
    visit_time[node] = time
    low[node] = time
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == True and parents[node]!= neighbour:
            low[node] = min(low[node], visit_time[neighbour])
        if visited[neighbour] == False:
            parents[neighbour] = node
            explore(graph, neighbour, visited, parents, visit_time, low, bridges)
            low[node] = min(low[node], low[neighbour])
    if low[node] == visit_time[node] and parents[node] != None:
        bridges.append((parents[node], node))


def DFS(graph, visited, parents, visit_time, low, bridges):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
        visit_time[v] = 0
        low[v] = inf
    global time
    time = 0
    for v in range(len(graph)):
        if visited[v] == False :
            explore(graph, v, visited, parents, visit_time, low, bridges)

a = Find_Bridges(Graph)
print(a)

