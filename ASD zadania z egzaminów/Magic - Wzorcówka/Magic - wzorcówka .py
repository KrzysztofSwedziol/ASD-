from egz2btesty import runtests

def magic( C ):
    n = len(C)
    memo = [-1 for i in range(n)]
    memo[0] = 0
    for i in range(n):
        if memo[i] == -1:
            continue
        gold_in_chest = C[i][0]
        for j in range(1,4):
            curr_chamber = C[i][j][1]
            gold_required = C[i][j][0]
            if curr_chamber == -1:
                continue
            if gold_in_chest > gold_required:
                if gold_in_chest - gold_required <= 10:
                    all_gold = gold_in_chest - gold_required + memo[i]
                    if all_gold > memo[curr_chamber]:
                        memo[curr_chamber] = all_gold

            if gold_in_chest < gold_required:
                if memo[i] >= gold_required - gold_in_chest:
                    all_gold = memo[i] - gold_required + gold_in_chest
                    if all_gold > memo[curr_chamber]:
                        memo[curr_chamber] = all_gold

            if gold_in_chest == gold_required:
                all_gold = memo[i]
                if all_gold > memo[curr_chamber]:
                    memo[curr_chamber] = all_gold


    return memo[n-1]


runtests( magic, all_tests = True )
