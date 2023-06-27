varlist=['adrik',20,40,20.1,'car']
for i in range(-1,-len(varlist)-1,-1):
    print(varlist[i],end=' ')
print('')
print(varlist[0])
print(varlist[len(varlist)-1])                          #prints the last element
print(varlist[-2])

print('')
print(varlist[0:4])
print(varlist[5:])
print(varlist[0:len(varlist)])
print(varlist[2:])
print(varlist[:])
print(varlist[::-1])
print(varlist[::2])

print(varlist.index('car'))