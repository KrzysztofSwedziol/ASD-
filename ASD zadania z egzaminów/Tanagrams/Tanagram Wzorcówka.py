def tanagram(word1, word2, t):
    dict = {}
    n = len(word1)
    for i in range(n):
        dict[word1[i]] = 0

    curr_window1 = 0
    curr_window2 = t
    for i in range(t + 1):
        dict[word1[i]] += 1

    flag = True
    for i in range(n):
        if curr_window2 == n:
            break
        curr_letter = word2[i]
        if dict[curr_letter] <= 0:
            flag = False
            break
        if dict[curr_letter] > 0:
            if curr_window2 + 1 <= n-1:
                curr_window2 = curr_window2 + 1
                dict[word1[curr_window2]] += 1
            if i - 3 > 0:
                dict[word1[curr_window1]] -= 1
                curr_window1 += 1

    return flag


word1 = "kotomysz"
word2 = "tokmysoz"
t = 3

print(tanagram(word1, word2, t))



