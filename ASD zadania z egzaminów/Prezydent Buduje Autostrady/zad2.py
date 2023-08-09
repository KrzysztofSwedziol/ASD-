from zad2testy import runtests
from math import sqrt


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

    return MST, edges, parents, rank

def new_kruskal(G, start, edges):
    n = len(G)
    MST = []
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    for i in range(start, len(edges)):
        if len(MST) >= n-1:
            break
        u = edges[i][0]
        v = edges[i][1]
        x = find(u, parents, rank)
        y = find(v, parents, rank)
        if x!=y:
            MST.append((u, v, edges[i][2]))
            union(x, y, parents, rank)
    if len(MST) < n-1:
        return None
    return MST


def distance_between_two(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
    new_dist = int(distance)
    if new_dist < distance:
        return new_dist + 1
    return distance

def create_graph(A):
    n = len(A)
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist = distance_between_two(A[i], A[j])
            if dist != 0:
                graph[i].append((j, dist))

    return graph

def highway(A):
    Graph = create_graph(A)
    MST, edges, parents, rank = Kruskal(Graph)
    n = len(edges)
    minimum = float('inf')
    for i in range(n):
        MST2 = new_kruskal(Graph, i, edges)
        if MST2 != None:
            if MST2[len(MST2) - 1][2] - MST2[0][2] < minimum:
                minimum = MST2[len(MST2) - 1][2] - MST2[0][2]

    return minimum
        

runtests( highway ) 
