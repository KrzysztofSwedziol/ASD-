#Time Complexity : O(n*w) n - number of elements in array ; w - number of digits in largest number

def RadixSort(tab):
    n = len(tab)
    max_val = max(tab)
    counter = 0
    while max_val > 0:
        max_val = max_val/10
        counter += 1

    new_tab = [[] for i in range(10)]


    for i in range(counter):
        for j in range(n):
            index = (tab[j] // 10**i)%10
            new_tab[index].append(tab[j])
        numerator = 0
        for k in range(10):
            for t in range(len(new_tab[k])):
                tab[numerator] = new_tab[k][t]
                numerator+=1
            new_tab[k] = []

    return tab

tab = [170, 45, 75, 90, 802, 24, 2, 66, 1000, 2137, 6969, 420, 3111, 3112, 421, 137]
print(tab)
print(RadixSort(tab))


