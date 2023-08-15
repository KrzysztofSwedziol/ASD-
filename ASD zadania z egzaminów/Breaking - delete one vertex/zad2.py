from zad2testy import runtests
from math import inf

def explore(graph, node, visited, parents):
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            parents[neighbour] = node
            explore(graph, neighbour, visited, parents)
    time +=1   #wierzchołek został przetworzony i time to czas przetworzenia

def DFS(graph):
    n = len(graph)
    visited = [False for i in range(n)]
    parents = [None for i in range(n)]
    counter = 0
    global time
    time = 0
    for v in range(len(graph)):
        if visited[v] == False :
            counter += 1
            explore(graph, v, visited, parents)
    return counter

def copy_graph(graph1, graph2):
    n = len(graph1)
    for i in range(n):
        for j in range(n):
            graph2[i][j] = graph1[i][j]

def change_graph(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                new_graph[i].append(j)

    return new_graph

def breaking(G):
    n = len(G)
    graph_copy = [[0 for i in range(n)]for i in range(n)]
    copy_graph(G, graph_copy)
    memo = [1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                G[i][j] = 0
                G[j][i] = 0

        new_graph = change_graph(G)
        amount = DFS(new_graph)
        memo[i] = amount
        for j in range(n):
            if graph_copy[i][j] == 1:
                G[i][j] = 1
                G[j][i] = 1

    maximum = 0
    index = 0
    for i in range(n):
        if memo[i] > maximum:
            maximum = memo[i]
            index = i

    if maximum == 1 or maximum == 2:
        return None

    return index


runtests( breaking )