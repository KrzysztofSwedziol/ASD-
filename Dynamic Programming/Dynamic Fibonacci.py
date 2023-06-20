#function gets number of the element in sequence and prints it
def fib(num):
    counter = 2
    tab = []
    tab.append(1)
    tab. append(1)
    while counter < num :
        tab.append(0)
        tab[counter] = tab[counter-1] + tab[counter-2]
        counter+=1
    return tab[num-1]
print(fib(7))

