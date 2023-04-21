# A-----------C\
# |           |  \
# |           |    \
# |           |     E
# |           |    /
# |           |  /
# B-----------D/

from collections import deque

# -------------------------List Graph with parameters without dictionaries-----------------------------------------------

# A--->0, B--->1, C--->2, D--->3, E--->4

graph = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]]
visited = [False for i in range(5)]
parents = [None for j in range(5)]
distance = [0 for k in range(5)]

for x in range(5):
    print(x, '--->', graph[x])


def BFS(graph, starting_node, visited, parents, distance):
    for v in range(len(graph)):
        visited[v] = False
        parents[v] = None
        distance[v] = 0
    queue = deque()
    queue.append(starting_node)
    visited[starting_node] = True
    while (len(queue) > 0):
        current_node = queue.popleft()

        print("current node : ", current_node)
        print("current node's distance from start : ", distance[current_node])
        print("current node's parent : ", parents[current_node])

        for neighbour in graph[current_node]:

            if visited[neighbour] == False:
                queue.append(neighbour)
                parents[neighbour] = current_node
                distance[neighbour] = distance[current_node] + 1
                visited[neighbour] = True


BFS(graph, 0, visited, parents, distance)