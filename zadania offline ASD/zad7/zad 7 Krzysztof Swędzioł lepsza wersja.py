#Krzysztof Swędzioł 418001
#Algorytm działa następująco - wiemy że jeśli w danym momencie w kolumnie o jeden na lewo mamy maksymalne wartości dla
#każdego z pól to jak przetestujemy wszystkie możliwości zaczynając od każdego pola z kolumny wcześniej to w kolumnie obecnej
#zawsze dostaniemy największe wartości. Można to jednak udoskonalić w taki sposób że zauważamy iż wystarczy raz przejść
#z góry na dół i zmieniać wartości idąc "wężykiem w dół" i przy każdym kroku powiększając wartość o jeden i potem porównywać
#ją z wartością na lewo powiększoną o jeden i wybierać tą większą, następnie zapisujemy tą kolumnę w jej kopii
#analogicznie postępujemy idąc z dołu na górę i na koniec porównujemy wartości z kopii kolumny z tymi obecnymi i zamieniamy
#na odpowiednie tam gdzie trzeba
#na koniec zwracamy wartość dla pola n-1 n-1
#Algorytm wykonuje swoje zadanie w czasie O(n^2)

from zad7testy import runtests


def maze(L):
    n = len(L)
    result_tab = [[float('inf') * -1 for i in range(n)] for j in range(n)]
    result_tab[0][0] = 0
    for k in range(1, n, 1):  # ustalenie pierwszej kolumny
        if L[k][0] != "#" and L[k - 1][0] != "#":
            result_tab[k][0] = result_tab[k - 1][0] + 1
        else:
            for m in range(k, n, 1):
                result_tab[m][0] = "#"
            break

    for i in range(1, n, 1):
        for j in range(n):  # jazda w dół
            if L[j][i] != "#":

                if result_tab[j][i - 1] != "#" and result_tab[j][i - 1] + 1 > result_tab[j][i]:
                    result_tab[j][i] = result_tab[j][i - 1] + 1

                if j - 1 >= 0 and result_tab[j - 1][i] != "#" and result_tab[j - 1][i] + 1 > result_tab[j][i]:
                    result_tab[j][i] = result_tab[j - 1][i] + 1

                if L[j - 1][i] == "#" and L[j][i - 1] == "#" and j + 1 <= n - 1 and L[j + 1][i] == "#":
                    result_tab[j][i] = "#"
            else:
                result_tab[j][i] = "#"

        copy_col = []  # kopia kolumny
        for z in range(n):
            copy_col.append(result_tab[z][i])

        # flag = False
        for g in range(n - 1, -1, -1):  # Jazda w górę
            if L[g][i] != "#" and result_tab[g][i] != "#":

                if result_tab[g][i - 1] != "#":
                    # flag = True
                    result_tab[g][i] = result_tab[g][i - 1] + 1
                else:
                    result_tab[g][i] = float('inf') * -1

                if g + 1 <= n - 1 and L[g + 1][i] != "#" and result_tab[g + 1][i] != "#" and result_tab[g + 1][i] + 1 > \
                        result_tab[g][i]:
                    result_tab[g][i] = result_tab[g + 1][i] + 1

                if result_tab[g][i - 1] == "#" and g + 1 <= n - 1 and i + 1 <= n - 1 and result_tab[g + 1][i] == "#" and \
                        result_tab[g][i + 1] == "#":
                    result_tab[g][i] = "#"
            else:
                result_tab[g][i] = "#"
                # flag = False

        for u in range(n):
            if copy_col[u] > result_tab[u][i]:
                result_tab[u][i] = copy_col[u]

    if result_tab[n - 1][n - 1] == "#":
        return -1
    if result_tab[n - 1][n - 1] == float('inf') * -1:
        return -1
    # for i in range(n):
    # print(result_tab[i])

    return result_tab[n - 1][n - 1]


runtests(maze, all_tests=True)