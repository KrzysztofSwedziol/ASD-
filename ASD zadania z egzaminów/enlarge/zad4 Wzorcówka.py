from zad4testy import runtests
from collections import deque
from math import inf

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

def create_path(graph, parents, t, s, new_graph):
    curr = t
    prev = t
    while curr != s:
        prev = parents[curr]
        if curr not in new_graph[prev]:
            new_graph[prev].append(curr)
            new_graph[curr].append(prev)
        curr = prev

def BFS2(graph, starting_node, t):
    n = len(graph)
    visited = [False for i in range(n)]
    parents = [None for i in range(n)]
    distance = [0 for i in range(n)]
    queue = deque()
    queue.append(starting_node)
    visited[starting_node] = True
    while (len(queue) > 0):
        current_node = queue.popleft()
        for neighbour in graph[current_node]:

            if visited[neighbour] == False:
                queue.append(neighbour)
                parents[neighbour] = current_node
                distance[neighbour] = distance[current_node] + 1
                visited[neighbour] = True
    return distance[t]

def BFS(graph, starting_node, t, shortest, new_graph):
    n = len(graph)
    visited = [False for i in range(n)]
    parents = [None for i in range(n)]
    distance = [0 for i in range(n)]
    queue = deque()
    queue.append(starting_node)
    visited[starting_node] = True
    while (len(queue) > 0):
        current_node = queue.popleft()
        for neighbour in graph[current_node]:

            if visited[neighbour] == False or neighbour == t:
                queue.append(neighbour)
                parents[neighbour] = current_node
                distance[neighbour] = distance[current_node] + 1
                visited[neighbour] = True
                if neighbour == t:
                    if distance[t] == shortest:
                        create_path(graph, parents, t, starting_node, new_graph)


def extract(graph, s, t, shortest):
    n = len(graph)
    new_graph = [[] for i in range(n)]
    BFS(graph, s, t, shortest, new_graph)
    return new_graph


def longer( G, s, t ):
    shortest = BFS2(G, s, t)
    shortest_paths = extract(G, s, t, shortest)
    a = Find_Bridges(shortest_paths)

    if len(a) == 0:
        return None
    return a[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )