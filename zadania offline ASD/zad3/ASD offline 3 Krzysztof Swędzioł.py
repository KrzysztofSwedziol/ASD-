#Krzysztof Swędzioł
#Algorytm działa następująco : przejeżdża po całej tablicy i każdym wyrazie i sprawdza czy ten pisany od tyłu jest
#leksykograficznie mniejszy niż pisany od przodu, jeśli tak, podmienia go na tą leksykograficznie mniejszą wersję
# - w ten sposób pozbywamy się potrzeby sprawdzania wyrazów od tyłu i od przodu bo np ze słów kot i tok tworzą się
#słowa kot i kot. Następnie używam Merge Sorta do posortowania tablicy leksykograficznie po wyrazach
#Ostatni etap algorytmu to przejechanie po całej tablicy i zliczanie ile jest obok siebie takich samych wyrazów
# a potem funkcja zwraca maximum z tego.
# Algorytm wykonuje swoje zadanie w czasie N + NlogN


from zad3testy import runtests

def Merge_Sort(tab):
    if len(tab)>1:
        mid = len(tab)//2
        tab_r=tab[:mid]
        tab_l=tab[mid:]

        Merge_Sort(tab_l)
        Merge_Sort(tab_r)

        i = 0
        j = 0
        k = 0
        while i < len(tab_r) and j < len(tab_l):
            if tab_r[i]<tab_l[j]:
                tab[k]=tab_r[i]
                i +=1
                k += 1

            else:
                tab[k]=tab_l[j]
                j+=1
                k+=1

        while i < len(tab_r):
            tab[k]=tab_r[i]
            i+=1
            k+=1
        while j < len(tab_l):
            tab[k]=tab_l[j]
            j+=1
            k+=1




def strong_string(T):
    n = len(T)
    for i in range(n):
        x = T[i]
        y = x[::-1]
        if y < x:
            T[i] = y

    Merge_Sort(T)

    max_counted = 0
    counter = 1
    for i in range(1, len(T), 1):
        if (T[i] == T[i - 1]):
            counter += 1
        else:
            max_counted = max(max_counted, counter)
            counter = 1

    return max_counted





    return -1


runtests(strong_string, all_tests=True)