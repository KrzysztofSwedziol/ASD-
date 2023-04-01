from zad3testy import runtests

def strong_string(T):

    n = len(T)

    def kwadratuj(napis):

        if napis[::-1] < napis:

            return napis[::-1]

        return napis

    def koduj(napis):

        kod = ord(napis[0]) + ord(napis[-1])
        kod *= len(napis)
        kod = kod**2 - ord(napis[0])
        kod = kod % n

        return kod

    def dodaj(tab, napis):

        index = koduj(napis)

        if tab[index][0] is None:
            tab[index][0] = [napis, 1]
            return 1

        else:

            for i in range(len(tab[index])):

                if tab[index][i][0] == napis:
                    tab[index][i][1] += 1
                    return tab[index][i][1]

            tab[index].append([napis, 1])
            return 1

    for i in range(len(T)):

        T[i] = kwadratuj(T[i])

    napisy = [[None] for _ in range(n)]

    wynik = 1
    for i in range(n):

        score = dodaj(napisy, T[i])

        if score > wynik:
            wynik = score

    return wynik


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
