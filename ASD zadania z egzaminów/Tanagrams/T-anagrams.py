word1 = "kotomysz"
word2 = "tokmysoz"

def Tuple_Merge(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        P = tab[mid:]
        Tuple_Merge(L)
        Tuple_Merge(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i][0] < P[j][0]:
                tab[k] = L[i]
                i += 1
                k += 1
            else:
                tab[k] = P[j]
                j += 1
                k += 1
        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1
        while j < len(P):
            tab[k] = P[j]
            j += 1
            k += 1


def word_to_tab(word):
    n = len(word)
    tab = []
    for i in range(n):
        tab.append((word[i], i))
    return tab

def tanagram(word1, word2, t):
    n = len(word1)
    word_tab1 = word_to_tab(word1)
    word_tab2 = word_to_tab(word2)

    Tuple_Merge(word_tab1)
    Tuple_Merge(word_tab2)

    print(word_tab1)
    print(word_tab2)

    maximum = 0
    for i in range(n):
        curr = abs(word_tab1[i][1] - word_tab2[i][1])
        if curr > maximum:
            maximum = curr
    if maximum == t:
        return True
    return False

print(tanagram(word1, word2, 3))
print(tanagram(word1, word2, 2))
