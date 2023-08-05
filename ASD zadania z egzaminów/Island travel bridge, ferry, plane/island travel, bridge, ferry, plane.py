from zad1testy import runtests
from math import inf
from queue import PriorityQueue

#rozbijam wierzchołki na 3 każdy i każdy z nich oznacza że do danego wierzchołka dojechałem albo mostem albo promem
#albo samolotem. Następnie odpalam Dijkstrę na nowym grafie.

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

def convert_curr(curr_index):
    return 3*curr_index


def create_graph(original, new_graph):
    n = len(original)
    for i in range(n):
        curr = i
        new_curr = convert_curr((curr))
        new_curr1 = new_curr       #arrived here by bridge 1B
        new_curr2 = new_curr + 1   #arrived here by ferry 5B
        new_curr3 = new_curr + 2   #arrived here by plane 8B
        for j in range(n):
            new_next = convert_curr(j)
            new_next1 = new_next
            new_next2 = new_next + 1
            new_next3 = new_next + 2
            if original[i][j] == 1:
                new_graph[new_curr2][new_next1] = 1
                new_graph[new_curr3][new_next1] = 1
            if original[i][j] == 5:
                new_graph[new_curr1][new_next2] = 5
                new_graph[new_curr3][new_next2] = 5
            if original[i][j] == 8:
                new_graph[new_curr1][new_next3] = 8
                new_graph[new_curr2][new_next3] = 8

def convert_to_list(graph):
    n = len(graph)
    list_graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                list_graph[i].append((j, graph[i][j]))
    return list_graph


def islands(G, A, B):
    n = len(G)
    new_graph = [[0 for k in range(3*n)] for i in range(3*n)]
    create_graph(G, new_graph)
    new_A1 = convert_curr(A)
    new_A2 = convert_curr(A) + 1
    new_A3 = convert_curr(A) + 2

    new_B1 = convert_curr(B)
    new_B2 = convert_curr(B) + 1
    new_B3 = convert_curr(B) + 2

    list = convert_to_list(new_graph)
    dis1 = Dijkstra(list, new_A1)
    dis2 = Dijkstra(list, new_A2)
    dis3 = Dijkstra(list, new_A3)

    minimum = inf
    minimum2 = inf
    minimum3 = inf
    minimum = min(dis1[new_B1], dis1[new_B2], dis1[new_B3])
    minimum2 = min(dis2[new_B1], dis2[new_B2], dis2[new_B3])
    minimum3 = min(dis3[new_B1], dis3[new_B2], dis3[new_B3])

    result = min(minimum, minimum2, minimum3)


    return result
        

runtests( islands ) 
