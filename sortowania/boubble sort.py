tab = [3,1,7,5,6,10,15,7,13,9,3,6,7]
print(tab)
def bouble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-2):
            if tab[j]>=tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]


bouble_sort(tab)
print(tab)
