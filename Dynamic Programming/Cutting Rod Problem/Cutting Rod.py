def Cut(rode_len, costs):
    memo = [0 for i in range(rode_len + 1)]
    for cost in costs:
        length = cost[0]
        c = cost[1]
        memo[length] = c

    for i in range(1, rode_len+1):
        for option in costs:
            length = option[0]
            c = option[1]
            if length <= i:
                curr = c + memo[i-length]
                if curr > memo[i]:
                    memo[i] = curr

    return memo[rode_len]

rode_length = 18
costs = [(3,3), (1,1), (5,8), (7,12)]

print(Cut(rode_length, costs))