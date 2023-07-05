dstudent={1:'adrik',2:'daniel',3:'alan',4:'arjun',5:'gaurij'}
dstudent[6]='martin'
print(dstudent)
dstudent.pop(3)                                     #it removes the key not the position
print(dstudent)
dstudent.popitem()
print(dstudent)
dstudent.clear()
print(dstudent)
dstudent.update({6:'arjun r',7:'rohit'})

dstud={3:'alan',4:'arjun',5:'gaurij'}
for i in dstud:
    print(i,end=' ')
print('')
for i in dstud:
    print(dstud[i],end=' ')
print('')
for i in dstud.keys():
    print(i,end=' ')
print('')
for i in dstud.values():
    print(i,end=' ')
print('')
for i in dstud.items():
    print(i,end=' ')
print('')
