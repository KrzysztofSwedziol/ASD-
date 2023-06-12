#Krzysztof Swędzioł 418001
#Algorytm działa następująco - tworzymy drzewo rekurencji w taki sposób że za każdym razem w każdym ruchu możemy pójść albo w prawo
#albo w dół albo w górę. Usprawnieniem algorytmu jest natomiast tablica 3d która służy do memoizacji wartości które już znamy
#na przykład załóżmy że przychodzimy z góry do pola [0][3] i w tablicy jest zapisana jakaś wartość to oznacza to że
#wartość ta odpowiada największej ilości komnat jakie możemy odwiedzić wychodząc z komnaty[0][3] jeśli przyszliśmy do niej
#z góry.
#Algorytm wykonuje swoje zadanie w czasie O(n^2)

from zad7testy import runtests


def travel(maze, n, pos1, pos2, last_move, from_where, result_tab):
    if pos1 == n - 1 and pos2 == n - 1:
        return 0

    if pos1 < 0 or pos1 > n - 1 or pos2 < 0 or pos2 > n - 1:
        return -1

    if maze[pos1][pos2] == "#":
        return -1

    if result_tab[from_where][pos1][pos2] != float("-inf"):
        return result_tab[from_where][pos1][pos2]

    if last_move == "up":

        max_value = max(travel(maze, n, pos1 - 1, pos2, "up", 0, result_tab),
                      travel(maze, n, pos1, pos2 + 1, "right", 2, result_tab))

        if (max_value == -1):
            result_tab[from_where][pos1][pos2] = -1
        else:
            result_tab[from_where][pos1][pos2] = max_value + 1

        return result_tab[from_where][pos1][pos2]

    if last_move == "down":
        max_value = max(travel(maze, n, pos1 + 1, pos2, "down", 1, result_tab),
                      travel(maze, n, pos1, pos2 + 1, "right", 2, result_tab))

        if (max_value == -1):
            result_tab[from_where][pos1][pos2] = -1
        else:
            result_tab[from_where][pos1][pos2] = max_value + 1

        return result_tab[from_where][pos1][pos2]

    if last_move == "right" or last_move == None:

        max_value = max(travel(maze, n, pos1 + 1, pos2, "down", 1, result_tab),
                      travel(maze, n, pos1 - 1, pos2, "up", 0, result_tab),
                      travel(maze, n, pos1, pos2 + 1, "right", 2, result_tab))

        if (max_value == -1):
            result_tab[from_where][pos1][pos2] = -1
        else:
            result_tab[from_where][pos1][pos2] = max_value + 1

        return result_tab[from_where][pos1][pos2]


def maze(L):
    n = len(L)
    result_tab = [[[float("-inf") for i in range(n)] for j in range(n)] for k in range(3)]
    #for i in range(n):
        #print("'",L[i],"'",",")
    travel(L, n, 0, 0, "down", 0, result_tab)
    if result_tab[0][0][0] == float("-inf"):
        return -1

    return result_tab[0][0][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)

