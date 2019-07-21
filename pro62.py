import sys
def palindrome(dk):
    if len(dk) == 1:
        return False
    if dk == dk[::-1]:
        return True
    return False
dk = input()
n1 = len(dk)
for i in range(n1-1, 0, -1):
    for j in range(0, n1-i):
        i1 = j
        i2 = j+i+1
        d2 = dk[i1:i2]
        if palindrome(d2):
            print(n1-len(d2))
            sys.exit()
