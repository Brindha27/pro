bk,st=map(str,input().split("|"))

cd=input()
if  len(bk)>len(st):
    if len(bk)==len(st)+len(cd):
        print(bk+"|"+st+cd)
elif len(bk)<len(st):
     if len(st)==len(bk)+len(cd):
        print(bk+cd+"|"+st)
elif len(bk)==len(st) and len(cd)>1 or (len(st) or len(bk)):
    print("impossible")
