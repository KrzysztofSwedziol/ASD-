#Krzysztof Swędzioł 418001
#Algorytm działa następująco : korzysta bezpośrenio z faktu że graf jest dwudzielny - zastępujemy tu Forda Fulkersona
#rekurencyjnym sprawdzaniem możliwości. Za każdym razem jak chcemy dołożyć następnego pracownika to sprawdzamy czy ma
#on jakieś wolne maszyny w "swoim zasięgu" jeśli tak to mu ją przypisujemy, jeśli natomiast nie, wywołujemy rekurencyjne
#sprawdzanie czy inni pracownicy mogą zmienić obecnie przypisane im maszyny w taki sposób aby jedna z maszyn z zasięgu
#pierwotnie sprawdzanego pracownika się zwolniła i aby ten mógł ją zająć
#dowód słuszności : załóżmy że w maksymalnym skojarzeniu nie ma przypisanego pracownika 1 do żadnej maszyny
#skoro tak jest to wszystkie maszyny z jego zasięgu są zajęte przez innych pracowników, skoro tak to jednego z
#zatrudnionych przy jakiejś maszynie pracowników można zwolnić i zastąpić go pracownikiem 1, co oznacza że algorytm działa
#gdyż tutaj za każdym razem pracownik pierwszy sprawdzany ma przypisywaną jakąś maszynę
#Algorytm wykonuje swoje działanie w czasie : O(VE)

from zad6testy import runtests

def Checker(human, M, n, visited, machines_reserved):

    for machine in M[human] :
        if visited[machine] == False:
            visited[machine] = True

            if machines_reserved[machine] == -1:
                machines_reserved[machine] = human
                return True
            else :
                visited[machine] = False

    for machine in M[human]:
        if visited[machine] == False:
            visited[machine] = True

            if machines_reserved[machine] == -1 or Checker(machines_reserved[machine], M, n, visited, machines_reserved):
                machines_reserved[machine] = human
                return True
    return False


def binworker(M):
    n = len(M)
    machines_reserved = [-1 for i in range(n)]
    max_work = 0
    for human in range(n):
        visited = [False for i in range(n)]
        if Checker(human, M, n, visited, machines_reserved):
            max_work +=1

    return max_work


    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )