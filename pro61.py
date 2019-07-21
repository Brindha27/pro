dk=str(input())
vh=str(input())
S=""
T1=0
T2=0
T=""
R=""
for X in range(0,len(dk)):
    T1=ord(dk[X])-96
    T2=ord(vh[X])+T1
    if(T2>122):
        T2=T2-122
        T2=T2+96
    T=T+chr(T2)
print(T)
