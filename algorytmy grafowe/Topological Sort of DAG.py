#    0 --> 1 --> 3
#    |     |
#    v     v
#    2 --> 4



from collections import deque

graph = [[1, 2], [3, 4], [4], [], []]
visited = [False for i in range(len(graph))]
parents = [None for j in range(len(graph))]

time = 0

def TopSort(G, visited, parents):
    sorted = []
    current = 0
    stack = deque()
    DFS(G, visited, parents, stack)
    while (len(stack)) > 0:
        current = stack.pop()
        sorted.append((current, [G[current]]))

    return sorted





def explore(graph, node, visited, parents, stack):
    global time
    time +=1   #wierzchołek został odwiedzony i time to czas odwiedzenia
    visited[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            parents[neighbour] = node
            explore(graph, neighbour, visited, parents, stack)
    time +=1   #wierzchołek został przetworzony i time to czas przetworzenia

    stack.append(node)


def DFS(graph, visited, parents, stack):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
    global time
    time = 0
    for v in range(len(graph)):
        if visited[v] == False :
            explore(graph, v, visited, parents, stack)

a = TopSort(graph, visited, parents)
print(a)