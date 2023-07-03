from egz2atesty import runtests

def coal( A, T ):
    magazines = [T]
    index = 0
    n = len(A)
    m = len(magazines)
    flag = False
    for i in range(n):
        for j in range(m):
            if magazines[j] - A[i] >= 0:
                magazines[j] -= A[i]
                flag = True
                index = j
                break
        if flag == False :
            magazines.append(T)
            m = len(magazines)
            index = m - 1
            magazines[m - 1] -= A[i]

        flag = False

    return index

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
