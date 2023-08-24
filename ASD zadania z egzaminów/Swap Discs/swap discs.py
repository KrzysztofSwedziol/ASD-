#from kolutesty import runtests


def explore(graph, node, visited, parents, disk, amounts, prev_disc, swaps):
    if amounts[node] == 0:
        visited[node] = True
        curr_disk = disk[node]
        if curr_disk != prev_disc:
            swaps[0] += 1
        for neighbour in graph[node]:
            amounts[neighbour] -= 1
        for neighbour in graph[node]:
            if visited[neighbour] == False:
                parents[neighbour] = node
                explore(graph, neighbour, visited, parents, disk, amounts, disk[node], swaps)


def DFS(graph, disk, amounts, start, starting_disk):
    n = len(graph)
    visited = [False for i in range(n)]
    parents = [None for i in range(n)]
    swaps = [0]
    explore(graph, start, visited, parents, disk, amounts, starting_disk, swaps)
    return swaps[0]




def create_graph(graph, depends):
    n = len(graph)
    for i in range(n):
        for j in range(len(depends[i])):
            curr_depend = depends[i][j]
            graph[curr_depend].append(i)

def add_amounts(amounts, depends):
    n = len(depends)
    for i in range(n):
        amounts[i] = len(depends[i])

def find_start(disk, depends):
    n = len(disk)
    for i in range(n):
        if len(depends[i]) == 0:
            return i, disk[i]


def swaps( disk, depends ):
    n = len(disk)
    graph = [[] for i in range(n)]
    amounts = [0 for i in range(n)]
    create_graph(graph, depends)
    add_amounts(amounts, depends)

    start, starting_disk = find_start(disk, depends)

    min_val = DFS(graph, disk, amounts, start, starting_disk)

    return min_val


#runtests( swaps, all_tests = True )

disk = ["A", "A", "B", "B"]
depends = [[2, 3], [], [1, 3], [1]]

print(swaps(disk, depends))


