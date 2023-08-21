tab = [3,6,8,2,1,8,6,15,10,11,7,3]
#[1,2,3,3,6,6,7,8,8,10,11,15]
print(tab)
print("zakres 1-15")


def Counting_Sort(tab):
    maximum = max(tab)
    tab2 = [0 for i in range(maximum + 1)]
    for i in range(len(tab)):
        tab2[tab[i]]+=1
    j=0
    for m in range(len(tab2)):
        while tab2[m]>0:
            tab[j]=m
            j+=1
            tab2[m]=tab2[m]-1

Counting_Sort(tab)
print(tab)
