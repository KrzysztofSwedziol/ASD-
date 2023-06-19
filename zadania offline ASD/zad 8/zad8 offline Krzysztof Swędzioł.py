#Krzysztof Swędzioł 418001
#Algorytm działa następująco : za każdym razem jak tankujemy pod danym indeksem to wydłużamy maksymalny zasięg
#od startu o tyle jaką wartość ma pole na którym tankujemy. Wybór pola polega na wyborze największej możliwej wartości w
#obecnym zasięgu, jeśli okaże się że suma zatankowanych wartości, która jest też zasięgiem,
#da nam wartość większą lub równą indeksowi docelowego
#pola to przerywamy działanie algorytmu i zwracamy licznik zatankowań gdyż oznacza to że z daną ilością paliwa
#jesteśmy w stanie dojechać od startu do końca.
#algorytm wykonuje swoje zadanie w czasie O(n*m)

from zad8testy import runtests

def explore(T, visited, n, m, new_road, curr1, curr2):
    if curr1 < 0 or curr1 >= n or curr2 < 0 or curr2 >= m :
        return 0
    if visited[curr1][curr2] == True:
        return 0
    if T[curr1][curr2] == 0 :
        visited[curr1][curr2] = True
        return 0

    visited[curr1][curr2] = True
    return T[curr1][curr2] + explore(T, visited, n, m, new_road, curr1-1, curr2) + \
        explore(T, visited, n, m, new_road, curr1+1, curr2) + explore(T, visited, n, m, new_road, curr1, curr2-1) + \
        explore(T, visited, n, m, new_road, curr1, curr2+1)



def DFS(T, visited, n, m, new_road, curr1, curr2):
    counter = 0
    position = 0
    neighbours = [(curr1 - 1, curr2), (curr1 + 1, curr2), (curr1, curr2 - 1), (curr1, curr2 + 1)]
    for i in range(m):
        counter = explore(T, visited, n, m, new_road, 0, i)
        new_road[i] += counter


def plan(T):
    n = len(T)
    m = len(T[1])
    new_road = [0 for i in range(m)]
    visited = [[False for i in range(m)] for j in range(n)]
    DFS(T, visited, n, m, new_road, 0, 0)

    loaded_fuel = new_road[0]
    new_road[0] = 0
    index = 0
    stops = 1
    max = 0
    for i in range(m):
        if loaded_fuel >= m-1:
            break
        for j in range(loaded_fuel+1):
            if new_road[j] > max:
                loaded_fuel -= max
                max = new_road[j]
                loaded_fuel += max
                index = j
        new_road[index] = 0
        max = 0
        index = 0
        stops += 1


    return stops




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

