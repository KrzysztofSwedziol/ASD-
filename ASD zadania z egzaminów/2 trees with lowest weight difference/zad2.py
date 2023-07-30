from zad2testy import runtests
from math import inf

def travel2(curr, nodes):
    n = len(curr.edges)
    if n == 0:
        return 0
    for i in range(n):
        nodes[curr][0] += curr.weights[i] + travel2(curr.edges[i], nodes)
    return nodes[curr][0]

def travel(curr, nodes):
    n = len(curr.edges)
    if n == 0:
        return

    for i in range(n):
        curr_node = curr.edges[i]
        curr_weight = curr.weights[i]
        curr_id = curr.ids[i]
        nodes[curr_node] = [0, curr_weight, curr_id]
        travel(curr_node, nodes)



def balance( T ):
    nodes = {}
    nodes[T] = [0, None, None]
    travel(T, nodes)
    travel2(T, nodes)
    biggest = 0
    best_divide = [-inf, inf]
    id_to_return = None
    for subtree in nodes:
        if nodes[subtree][0] > biggest:
            biggest = nodes[subtree][0]
    for sub in nodes:
        curr_sub = nodes[sub][0]
        curr_edge = nodes[sub][1]
        curr_id = nodes[sub][2]
        if curr_sub != biggest:
            if abs((biggest - curr_sub - curr_edge) - curr_sub ) < abs(best_divide[1] - best_divide[0]):
                best_divide[1] = biggest - curr_sub - curr_edge
                best_divide[0] = curr_sub
                id_to_return = curr_id

    return id_to_return

    
runtests( balance )


