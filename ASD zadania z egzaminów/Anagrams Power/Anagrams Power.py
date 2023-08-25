from kol1btesty import runtests

def Merge_Sort(tab):
    if len(tab)>1:
        mid=len(tab)//2
        L=tab[:mid]
        P=tab[mid:]
        Merge_Sort(L)
        Merge_Sort(P)

        i=j=k=0
        while i<len(L) and j<len(P):
            if L[i]<=P[j]:
                tab[k]=L[i]
                i+=1
                k+=1
            else:
                tab[k]=P[j]
                j+=1
                k+=1
        while i<len(L):
            tab[k]=L[i]
            i+=1
            k+=1
        while j<len(P):
            tab[k]=P[j]
            j+=1
            k+=1

def Counting_Sort(tab):
    maximum = max(tab)
    word_to_num = ord(maximum)
    tab2 = [0 for i in range(word_to_num - ord('a') + 2)]
    for i in range(len(tab)):
        curr = ord(tab[i]) - ord('a')
        tab2[curr]+=1
    j=0
    for m in range(len(tab2)):
        while tab2[m]>0:
            tab[j]=chr(m + ord('a'))
            j+=1
            tab2[m]=tab2[m]-1

def convert(word):
    n = len(word)
    tab = []
    for i in range(n):
        tab.append(word[i])
    Counting_Sort(tab)
    new_word = ''
    for i in range(n):
        new_word = new_word + tab[i]
    return new_word

def f(T):
    n = len(T)

    for i in range(n):
        curr_word = T[i]
        new_word = convert(curr_word)
        T[i] = new_word
    Merge_Sort(T)

    maximum = 1
    curr = 1
    for i in range(1, n):
        if T[i] == T[i-1]:
            curr+=1
            if curr > maximum:
                maximum = curr
        else :
            curr = 1


    return maximum



runtests( f, all_tests=True  )
