#Krzysztof Swędzioł
#Algorytm działa w taki sposób że iteruje po elementach danego słowa i sprawdza czy obecny element który jest środkiem
#potencjalnego palindromu ma szansę stworzyć palindrom dłuższy od obecnie najdłuższego - mając długość w danej chwili
#najdłuższego palindromu badamy czy słowo stworzone od środkowego, obecnie iterowanego elementu o indeksie i i końcach
#w indeksach i-((długość najdłuższego-1)//2) oraz i+((długość najdłuższego-1)//2) jest palindromem, jeżeli tak, oznacza
#to że jest albo tej samej długości co obecnie najdłuższy palindrom, albo jeszcze dłuższy-liczymy jego długość i zapisujemy
#jako nowy najdłuższy palindrom, jeżeli nie jest palindromem - przerywamy działanie pętli sprawdzających i wracamy do
#pętli głównej funkcji ceasar przechodząc do następnego elementu do zbadania.
#postępując w ten sposób zawsze znajdziemy szukany palindrom
#algorytm ten jest możliwy tylko dlatego że długość szukanego palindromu jest nieparzysta!
#algorytm wykonuje swoje zadanie w czasie O(n^2)

from zad1testy import runtests

def ceasar( s ):
    obecna_dlugosc=0
    najdluzszy=1
    for i in range(len(s)):
        if (len(s)-1-i)<=(najdluzszy-1)//2:
            break
        z=(najdluzszy-1)//2
        j=i-z
        k=i+z
        while 0<=j and k<len(s):
            if s[j]==s[k] and j<k:
                obecna_dlugosc+=2
                j+=1
                k-=1
            else:
                break
        if j==k and obecna_dlugosc+1==najdluzszy:
            j=i-z
            k=i+z
            while 0<=j-1 and k+1<len(s):
                if s[j-1]==s[k+1]:
                    najdluzszy+=2
                    j-=1
                    k+=1
                else:
                    break
        obecna_dlugosc=0
    return najdluzszy
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )