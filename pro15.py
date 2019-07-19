def countt_1(no) :
    ssss1 = bin(no)[2:]
    kss = ssss1.count('1')
    return kss
no = int(input())
Lo = [ int(x) for x in input().split()]
Los2 = []
for i in range(0,no) :
    Los2.append((countt_1(Lo[i]),Lo[i]))
Lo3 = sorted(Los2, key=lambda x : (x[0],x[1]),reverse=True)
Lo4 = [x[1] for x in Lo3 ]
for i in range(0,len(Lo4)) :
    print(Lo4[i])
