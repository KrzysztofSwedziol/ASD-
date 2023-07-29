from zad3testy import runtests

def update_status(lamps_status, operation):
    start = operation[0]
    end = operation[1]
    counter_before = 0
    counter_after = 0
    for i in range(start, end+1):
        if lamps_status[i]%3 == 2:
            counter_before += 1
        lamps_status[i] +=1
        if lamps_status[i]%3 == 2:
            counter_after += 1
    return counter_before, counter_after

def lamps( n,T ):
    length = len(T)
    maximum = 0
    curr = 0
    lamps_status = [0 for i in range(n)]
    for i in range(length):
        before, after = update_status(lamps_status, T[i])
        curr = curr - before + after
        if curr > maximum:
            maximum = curr
       
    return maximum

    
runtests( lamps )


