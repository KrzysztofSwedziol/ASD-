#Krzysztof Swędzioł 418001
#Algorytm działa następująco : analogicznie jak dla problemu plecakowego dla każdej pozycji w tablicy memo sprawdzamy
#dwie opcje - pierwsza oznacza że dla memo[j][i] - bierzemy to co było najlepsze dla i biurowców i j-1 działek
#druga opcja oznacza że sprawdzamy najlepszą opcję przy założeniu że dla i-tego biurowca bierzemy j-tą działkę
#cofamy się wówczas w memo do pola memo[j-1][i-1] która przechowuje najmniejsze długości dla i-1 biurowców
#i j-1 działek.
#Na koniec zwracam wartość memo[m-1][n-1] która zawiera najlepszy przydział m działek do n biurowców
#Nie trzeba sprawdzać warunku czy działki dla i są dalej od działek przydzielonych do i-1 ponieważ ten warunek w tym
#wykonaniu algorytmu jest zawsze spełniony - rozważmy dwie dowolne działki - jedna x1-----y1----y2----x2
#Nie ma możliwości żeby x2 została przydzielona dalsza działka bo jest ona zarezerwowana dla x1
#Algorytm działa w czasie O(m*n)

from egz2btesty import runtests

def parking(X,Y):
  n = len(X)
  m = len(Y)
  memo = [[float('inf') for i in range(n)] for j in range(m)]

  memo[0][0] = abs(X[0] - Y[0])
  for i in range(1, m):
    dist = abs(X[0] - Y[i])
    if dist < memo[i-1][0]:
      memo[i][0] = dist
    else:
      memo[i][0] = memo[i-1][0]


  for i in range(1, n):
    office = i
    for j in range(i, m):
      first_option = float('inf')
      second_option = float('inf')
      if j-1 >= 0:
        first_option = memo[j-1][i]
      if i-1 >= 0 :
        second_option = abs(X[i] - Y[j])
        second_option += memo[j-1][i-1]
      memo[j][i] = min(first_option, second_option)

  return memo[m-1][n-1]
  pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
