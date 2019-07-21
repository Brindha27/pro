Dk=input()
Qt=[]
for X in Dk:
  if X not in Qt:
    Qt.append(X)
  else:
    break  
print(len(Qt))
