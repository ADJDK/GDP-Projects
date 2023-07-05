nestlst=((1,2,3),(4,5,6),(7,8,9))
s=c=0
for n in nestlst:
    for i in n:
        s+=i 
        c+=1
print('the sum is',s)
print('the no of elements in the list is',c)
print(len(nestlst))
