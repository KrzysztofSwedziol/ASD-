#Krzysztof Swędzioł 418001

from zad6testy import runtests
def bfs(M, matchR, dist):
    n = len(M)
    queue = []
    for human in range(n):
        if matchR[human] == -1:
            dist[human] = 0
            queue.append(human)
        else:
            dist[human] = float('inf')
    dist.append(float('inf'))
    while queue:
        human = queue.pop(0)
        if dist[human] < dist[-1]:
            for machine in M[human]:
                next_human = matchR[machine]
                if dist[next_human] == float('inf'):
                    dist[next_human] = dist[human] + 1
                    queue.append(next_human)
    return dist[-1] != float('inf')

def dfs(human, M, matchR, dist):
    if human is not None:
        for machine in M[human]:
            next_human = matchR[machine]
            if dist[next_human] == dist[human] + 1 and dfs(next_human, M, matchR, dist):
                matchR[machine] = human
                return True
        dist[human] = float('inf')
        return False
    return True

def binworker(M):
    n = len(M)
    matchR = [-1] * n
    while True:
        dist = [None] * n
        if not bfs(M, matchR, dist):
            break
        for human in range(n):
            if matchR[human] == -1:
                dfs(human, M, matchR, dist)
    return sum([match != -1 for match in matchR])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )