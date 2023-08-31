from zad2testy import runtests
from queue import PriorityQueue
from math import inf
#0 - right 0 speed, 1 - bottom 0 speed 2- left 0 speed, 3 - up 0 speed, 4- right 1 speed ......

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

def maze_to_graph(maze):
    n = len(maze)
    m = len(maze[0])
    graph = [[] for i in range(n*m)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] != "X":
                curr_node = i*m + j
                if i-1 >=0 and maze[i-1][j] != "X":
                    neigh1 = (i-1)*m + j
                    graph[curr_node].append(neigh1)
                if j-1 >=0 and maze[i][j-1] != "X":
                    neigh2 = curr_node - 1
                    graph[curr_node].append(neigh2)
                if i + 1 <= n-1 and maze[i+1][j] != "X":
                    neigh3 = (i+1)*m + j
                    graph[curr_node].append(neigh3)
                if j+1 <= m-1 and maze[i][j+1] != "X":
                    neigh4 = curr_node + 1
                    graph[curr_node].append(neigh4)
    return graph

def convert_graph(graph, maze):
    k = len(maze)
    z = len(maze[0])
    n = len(graph)
    new_graph = [[] for i in range(12*n)]
    for i in range(n):
        curr_in_new = i*12
        new_graph[curr_in_new].append((curr_in_new + 1, 45))
        new_graph[curr_in_new].append((curr_in_new + 3, 45))
        new_graph[curr_in_new + 1].append((curr_in_new, 45))
        new_graph[curr_in_new + 1].append((curr_in_new + 2, 45))
        new_graph[curr_in_new + 2].append((curr_in_new + 1, 45))
        new_graph[curr_in_new + 2].append((curr_in_new + 3, 45))
        new_graph[curr_in_new + 3].append((curr_in_new + 2, 45))
        new_graph[curr_in_new + 3].append((curr_in_new, 45))

        new_graph[curr_in_new + 4].append((curr_in_new + 1, 45))
        new_graph[curr_in_new + 4].append((curr_in_new + 3, 45))
        new_graph[curr_in_new + 5].append((curr_in_new, 45))
        new_graph[curr_in_new + 5].append((curr_in_new + 2, 45))
        new_graph[curr_in_new + 6].append((curr_in_new + 1, 45))
        new_graph[curr_in_new + 6].append((curr_in_new + 3, 45))
        new_graph[curr_in_new + 7].append((curr_in_new, 45))
        new_graph[curr_in_new + 7].append((curr_in_new + 2, 45))

        new_graph[curr_in_new + 8].append((curr_in_new + 1, 45))
        new_graph[curr_in_new + 8].append((curr_in_new + 3, 45))
        new_graph[curr_in_new + 9].append((curr_in_new, 45))
        new_graph[curr_in_new + 9].append((curr_in_new + 2, 45))
        new_graph[curr_in_new + 10].append((curr_in_new + 1, 45))
        new_graph[curr_in_new + 10].append((curr_in_new + 3, 45))
        new_graph[curr_in_new + 11].append((curr_in_new, 45))
        new_graph[curr_in_new + 11].append((curr_in_new + 2, 45))

    for i in range(n):
        curr_in_new = 12 * i
        for j in range(len(graph[i])):
            neigh = graph[i][j]
            neigh_in_new = 12*neigh
            if neigh == i + 1:
                new_graph[curr_in_new].append((neigh_in_new + 4, 60))
                new_graph[curr_in_new + 4].append((neigh_in_new + 8, 40))
                new_graph[curr_in_new + 8].append((neigh_in_new + 8, 30))
            if neigh == i-1:
                new_graph[curr_in_new + 2].append((neigh_in_new + 6, 60))
                new_graph[curr_in_new + 6].append((neigh_in_new + 10, 40))
                new_graph[curr_in_new + 10].append((neigh_in_new + 10, 30))
            if neigh == i - z:
                new_graph[curr_in_new + 3].append((neigh_in_new + 7, 60))
                new_graph[curr_in_new + 7].append((neigh_in_new + 11, 40))
                new_graph[curr_in_new + 11].append((neigh_in_new + 11, 30))
            if neigh == i + z:
                new_graph[curr_in_new + 1].append((neigh_in_new + 5, 60))
                new_graph[curr_in_new + 5].append((neigh_in_new + 9, 40))
                new_graph[curr_in_new + 9].append((neigh_in_new + 9, 30))

    return new_graph



def robot( L, A, B ):
    n = len(L)
    m = len(L[0])

    graph = maze_to_graph(L)
    new_graph = convert_graph(graph, L)
    A_in_graph = A[1] * m + A[0]
    new_A = 12*A_in_graph
    B_in_graph = B[1] * m + B[0]
    new_B = 12*B_in_graph

    dist = Dijkstra(new_graph, new_A)

    min_dist = inf
    for i in range(12):
        if min_dist > dist[new_B + i]:
            min_dist = dist[new_B + i]
    if min_dist == inf:
        return None
    return min_dist

    
runtests( robot )


