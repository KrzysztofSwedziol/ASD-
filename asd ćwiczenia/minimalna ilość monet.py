coins = [1,2,7,10]
value = [float('inf') for i in range(16)]
value[0] = 0
value[1] = 1
for i in range(2, 16):
    for j in range(len(coins)) :
        if value[i-coins[j]]+1 < value[i]:
            value[i] = value[i-coins[j]] + 1

print(value[15])
print(value)

