from kol2testy import runtests

def compare(tab1, tab2):
    flag = True
    n = len(tab1)
    for i in range(n):
        if tab1[i] != tab2[i]:
            flag = False
    return flag

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

def NewKruskal(G, edges):
    n = len(G)
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    MST = []
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
        curr = NewKruskal(G, curr_edges)
        if len(curr) == edges_amount:
            for k in range(edges_amount):
                curr_sum += curr[k][2]
            return curr_sum


    return None


runtests( beautree, all_tests = True )
