from math import inf

graph = [
    [0, 3, 8, inf, -4],
    [inf, 0, inf, 1, 7],
    [inf, 4, 0, inf, inf],
    [2, inf, -5, 0, inf],
    [inf, inf, inf, 6, 0]
]


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

    for i in range(n):
        print(distance[i])

    return distance, parent

Floyd_Warshall(graph)
