# A-----------C\
# |           |  \
# |           |    \
# |           |     E
# |           |    /
# |           |  /
# B-----------D/

#-------------------------List Graph with parameters without dictionaries-----------------------------------------------

#A--->0, B--->1, C--->2, D--->3, E--->4

graph = [[1,2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]]
visited = [False for i in range(5)]
parents = [None for j in range(5)]

for x in range(5):
    print(x, '--->', graph[x])

time = 0


def explore(graph, node):
    print("current node : ", node)
    print("current node's parent : ", parents[node])
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    print(time)
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            parents[neighbour] = node
            explore(graph, neighbour)
    time +=1   #wierzchołek został przetworzony i time to czas przetworzenia

def DFS(graph, visited, parents):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
    global time
    time = 0
    for v in range(len(graph)):
        if visited[v] == False :
            explore(graph, v)


DFS(graph, visited, parents)