from zad2testy import runtests

def check(block1, block2):
    x1 = block1[0]
    y1 = block1[1]
    x2 = block2[0]
    y2 = block2[1]
    if x1 >= x2 and y1 <= y2:
        return True
    return False

def tower(A):
    n = len(A)
    memo = [1 for i in range(n)]
    for i in range(1, n):
        curr = A[i]
        best_for_i = 1
        for j in range(i-1, -1, -1):
            prev = A[j]
            if check(curr, prev):
                if memo[j] + 1 > best_for_i:
                    best_for_i = memo[j] + 1
            memo[i] = best_for_i        

    return max(memo)


runtests( tower )
