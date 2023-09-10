#Krzysztof Swędzioł 418001
#Algorytm działa następująco : dla każdego z punktów przejeżdżamy po całej tablicy i sprawdzamy każdy punkt z wykluczeniem
#obecnego czy jest dominowany przez obecny. Jeśli tak to counter powiększamy o 1. Operację wykonujemy dla każdego punktu
#i zwracamy maksiumu z tablicy w której zapisaliśmy wartości dla każdego punktu
#Algorytm wykonuje swoje zadanie w czasie O(n^2)

from egz2atesty import runtests

def dominance(P):
  n = len(P)
  memo = [0 for i in range(n)]
  for i in range(1, n):
    curr1 = P[i][0]
    curr2 = P[i][1]
    counter = 0
    for j in range(i-1, -1, -1):
      prev1 = P[j][0]
      prev2 = P[j][1]
      if curr1 > prev1 and curr2 > prev2:
        counter += 1
        #if memo[j] + 1 > memo[i]:
           #memo[i] = memo[j] + 1
    for k in range(i+1, n):
      next1 = P[k][0]
      next2 = P[k][1]
      if curr1 > next1 and curr2 > next2:
        counter += 1
    memo[i] = counter

  maximum = max(memo)
  return maximum

  pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
