from zad2testy import runtests
def add_prefixes(napis, dic):
    n = len(napis)
    for i in range(n):
        curr = napis[0:i+1]
        dic[curr] = 0

def add_prefixes2(napis, dic):
    n = len(napis)
    for i in range(n):
        curr = napis[0:i+1]
        dic[curr] +=1

def alter_prefixes(dic):
    new_dic = {}
    for prefix in dic:
        alter1 = prefix + "1"
        alter2 = prefix + "0"
        new_dic[alter1] = 0
        new_dic[alter2] = 0
    for pre in new_dic:
        dic[pre] = new_dic[pre]

def double_prefix( L ):
    dic = {}
    for napis in L:
        add_prefixes(napis, dic)
    alter_prefixes(dic)
    for napis in L:
        add_prefixes2(napis, dic)

    prefixes = []
    for prefix in dic:
        amount = dic[prefix]
        if amount >= 2:
            alter1 = prefix + "0"
            alter2 = prefix + "1"
            if dic[alter1] < 2 and dic[alter2] < 2:
                prefixes.append(prefix)



    return prefixes


runtests( double_prefix )

