from kol2testy import runtests
from collections import deque

def is_ok(visited):
    n = len(visited)
    flag = True
    for i in range(n):
        if visited[i] == False:
            flag = False
    return flag


def BFS(graph, starting_node):
    visited = [False for i in range(len(graph))]
    parents = [None for i in range(len(graph))]
    distance = [0 for i in range(len(graph))]
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
    return visited


def create_graph(edges):
    n = len(edges)
    new_graph = [[] for i in range(n+1)]
    for i in range(n):
        v1 = edges[i][0]
        v2 = edges[i][1]
        new_graph[v1].append(v2)
        new_graph[v2].append(v1)

    return new_graph


def find(v, parents, rank):
    if parents[v] != v:
        parents[v] = find(parents[v], parents, rank )
    return parents[v]

def union(set1, set2, parents, rank):
    x = find(set1, parents, rank)
    y = find(set2, parents, rank)
    if rank[x] > rank[y]:
        parents[y] = x
        return x
    else :
        parents[x] = y
        if rank[y] == rank[x]:
            rank[y] +=1
        return y

def Kruskal(G):
    n = len(G)
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    edges = []
    MST = []
    for i in range(n):
        for v, c in G[i]:
            if i < v:
                edges.append((i, v, c))
    edges.sort(key = lambda x: x[2])
    for i in range(len(edges)):
        if len(MST) >= n-1:
            break
        u = edges[i][0]
        v = edges[i][1]
        x = find(u, parents, rank)
        y = find(v, parents, rank)
        if x!=y:
            MST.append((u, v, edges[i][2]))
            union(x, y, parents, rank)

    return MST, edges

def beautree(G):
    MST, edges = Kruskal(G)
    n = len(edges)
    m = len(G)
    edges_amount = m-1
    curr_sum = 0
    for i in range(n):
        if i + edges_amount > n - 1:
            break
        curr_edges = edges[i:(i+edges_amount)]
        new_graph = create_graph(curr_edges)
        visited = BFS(new_graph, 0)
        if is_ok(visited):
            for i in range(len(curr_edges)):
                curr_sum += curr_edges[i][2]
            return curr_sum



    return None


runtests( beautree, all_tests = True )
