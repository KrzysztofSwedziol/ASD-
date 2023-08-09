#Works on list graph representation

# A-----5------C\
# |           |  6
# |           |    \
# 8           2     E
# |           |    /
# |           |  9
# B-----3------D/
graph = [[(1,8), (2, 5)], [(0, 8), (3, 3)], [(0, 5), (3, 2), (4, 6)], [(1, 3), (2, 2), (4, 9)], [(2, 6), (3, 9)]]

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

    return MST
print(Kruskal(graph))
