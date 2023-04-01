#Krzysztof Swędzioł
#jeszcze przed użyciem algorytmu trzeba zauważyć zależność iż wybór elementów dających największą możliwą sumę
#przed ich całkowitym roztopieniem to de facto wybór pewnej liczby k elementów największych i zsumowanie ich z uwzględnieniem
#ilości stopnień. Na przykład dla tablicy [1,7,3,5,8,2,9,6,10], która po posortowaniu wygląda tak : [1,2,3,5,6,7,8,9,10]
#możemy zabrać następująco : 10 + (9-1) + (8-2) + (7-3) + (6-4) = 30. Można zauważyć że te k elementów największych
#zawsze da się zebrać w dowolnie nieuporządkowanej tablicy ale kolejność ich zbierania będzie inna lecz to nie
#przeszkadza bo ostatecznie dadzą tą samą sumę.
#ALGORYTM to tak naprawdę przekształcony Heap Sort z wykładu - najpierw układa tablicę w kopiec i potem w końcowym
#etapie gdy zbiera ze szczytu kopca największy w danej chwili element, dodaje go pomniejszonego o ilość stopnień do
#sumy, gdy elementy pomniejszone o ilość stopnień zaczynają być mniejsze lub równe zero, algorytm przerywa działanie
#i zwraca sumę (nie ma sensu sortować całej tablicy gdyż interesuje nas tylko suma k początkowych elementów pomniejszona
#o odpowiednią ilość stopnień każdego z nich).
#Algorytm wynkonuje swoje działanie w czasie O(nlogn).

from zad2testy import runtests
def left(i):
    return 2*i +1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

def heapify(tab, i, n):
    L=left(i)
    R=right(i)
    max_ind=i
    if L<n and tab[L]>tab[i]:
        max_ind=L
    if R<n and tab[R]>tab[max_ind]:
        max_ind=R
    if max_ind != i:
        tab[max_ind], tab[i]=tab[i], tab[max_ind]
        heapify(tab, max_ind, n)

def build_heap(tab):
    n=len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n )

def heap_sort(tab):
    n=len(tab)
    melt_counter=0
    sum=0
    build_heap(tab)
    for i in range(n-1, 0, -1):
        tab[i], tab[0]=tab[0], tab[i]
        if (tab[i]-melt_counter)>0:
            sum=sum+(tab[i]-melt_counter)
            melt_counter+=1
            heapify(tab, 0, i)
        else:
            break
    return sum

def snow( S ):
    a=heap_sort(S)
    return a

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )