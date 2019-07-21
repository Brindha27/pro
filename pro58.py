import sys
n1 = int(input())
ds = []
if n1 == 2:
    print('3')
    print('2 1 2')
    sys.exit()
if n1 == 3:
    print('4')
    print('2 1 3 2')
    sys.exit()
k = n1//2
for i in range(2, n1+1, 2):
    ds.append(i)

for i in range(1, n1, 2):
    ds.append(i)

for i in range(2, n1+1, 2):
    ds.append(i)
print(len(ds))
print(*ds)
