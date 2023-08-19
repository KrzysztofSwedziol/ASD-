from math import inf
from queue import PriorityQueue

def relax(G, s, node, neighbour_num, distance, parents, node_to_neigh, PriorQ ):
    if distance[neighbour_num] > distance[node] + node_to_neigh:
        distance[neighbour_num] = distance[node] + node_to_neigh
        parents[neighbour_num] = node
        PriorQ.put((distance[neighbour_num], neighbour_num))



def Dijkstra(G, s):
    parents = [None for i in range(len(G))]
    distance = [inf for j in range(len(G))]
    distance[s] = 0
    PriorQ = PriorityQueue()
    PriorQ.put((0, s))
    while PriorQ.qsize() > 0:
        curr = PriorQ.get()
        node = curr[1]
        for neighbour in (G[node]):
            node_to_neigh = neighbour[1]
            neighbour_num = neighbour[0]
            relax(G, s, node, neighbour_num, distance,parents,  node_to_neigh, PriorQ)
    return distance


def rewrite_graph(graph1, graph2):
    n = len(graph1)
    for i in range(n):
        curr_in_new1 = 2 * i
        curr_in_new2 = 2 * i + 1
        for j in range(n):
            curr_neigh1 = 2*j
            curr_neigh2 = 2*j + 1
            if graph1[i][j] != 0:
                graph2[curr_in_new1].append([curr_neigh1, graph1[i][j]])
                graph2[curr_in_new2].append([curr_neigh1, graph1[i][j]])

        for j in range(n):
            if graph1[i][j] != 0:
                value = graph1[i][j]
                for k in range(n):
                    curr_further1 = 2*k
                    curr_further2 = 2*k + 1
                    if graph1[j][k] != 0:
                        if k != i:
                            edge_cost = max(value, graph1[j][k])
                            graph2[curr_in_new1].append([curr_further2, edge_cost])





def jumper(G, s, w):
    n = len(G)
    new_graph = [[] for i in range(2*n)]  #1 - came to vertex without shoes, 2 - came to vertex with shoes
    rewrite_graph(G, new_graph)

    curr_s = s
    curr_w1 = 2*w
    curr_w2 = 2*w + 1
    tab = Dijkstra(new_graph, curr_s)

    return min(tab[curr_w1], tab[curr_w2])

graph = [[0 for i in range(5)] for j in range(5)]

graph[0][1] = 1
graph[1][0] = 1
graph[1][2] = 1
graph[2][1] = 1
graph[2][3] = 7
graph[3][2] = 7
graph[3][4] = 8
graph[4][3] = 8

print(jumper(graph, 0, 4))