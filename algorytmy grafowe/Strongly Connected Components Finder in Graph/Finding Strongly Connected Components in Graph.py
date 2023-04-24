from collections import deque

Graph = [[1], [2], [0, 3, 8], [4, 6], [5], [3], [5], [8], [9], [10], [7, 3]]

def Strongly_Connected(G):
    time = 0
    visited = [False for i in range(len(G))]
    parents = [False for j in range(len(G))]
    times = [0 for k in range(len(G))]
    stack = deque()
    DFS(G, visited, parents, times, stack)
    connected_tab = []
    G_reversed = Reverse_Edges(G)
    DFS2(G_reversed, visited, parents, times, stack, connected_tab)
    return connected_tab


def Reverse_Edges(G):
    new_G = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in G[i]:
            new_G[j].append(i)
    return new_G



def explore(graph, node, visited, parents, times, stack):
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            parents[neighbour] = node
            explore(graph, neighbour, visited, parents, times, stack)
    time +=1   #wierzchołek został przetworzony i time to czas przetworzenia
    times[node] = time
    stack.append(node)

def DFS(graph, visited, parents, times, stack):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
    global time
    time = 0
    for v in range(len(graph)):
        if visited[v] == False :
            explore(graph, v, visited, parents, times, stack)



def explore2(graph, node, visited, parents, times, b):
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            parents[neighbour] = node
            explore2(graph, neighbour, visited, parents, times, b)
    time +=1   #wierzchołek został przetworzony i time to czas przetworzenia
    times[node] = time
    b.append(node)



def DFS2(graph, visited, parents, times, stack, connected_tab):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
    global time
    time = 0
    while len(stack) > 0:
        a = stack.pop()
        if visited[a] == False:
            b = []
            explore2(graph, a, visited, parents, times, b)
            connected_tab.append(b)

a = Strongly_Connected((Graph))

print(a)


