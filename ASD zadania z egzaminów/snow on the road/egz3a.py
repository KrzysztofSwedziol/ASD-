from egz3atesty import runtests
def add_road(tab, curr_road):
    start = curr_road[0]
    end = curr_road[1]
    while start != end:
        tab[start] += 1
        start += 1
    tab[end] += 1

def snow( T, I ):
    n = len(I)
    tab = [0 for i in range(T)]
    for i in range(n):
        add_road(tab, I[i])
    maximum = max(tab)

    return maximum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
