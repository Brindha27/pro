def sub(aa): 
    n = len(aa) 
    sub = [1]*n 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if aa[i] > aa[j] and sub[i]< sub[j] + 1 : 
                sub[i] = sub[j]+1
    maximum = 0
    for i in range(n): 
        maximum = max(maximum , sub[i])  
    return maximum




ar=int(input()) 
aa = list(map(int,input().split()))
print (sub(aa))
