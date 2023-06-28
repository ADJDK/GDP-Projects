tup=('adrik','car','nice')
print(tup[0])
print(tup[-1])
print(tup[:2])
print(len(tup))
print(type(tup))
print('')

t=(1,2,3,4)
e=(1.2,1.4,5.6,25.6)
z=('things','some','water')
a=('cars',1.20,'fish','money')
print(a)
addi=t+z+e+a 
print(addi)
print('')

tuplee=('me','yuu','the','world')
for i in tuplee:
    print(i)
print('')

tupl=('see','we me','pilot')
i=0 
while i<len(tupl):
    print(tupl[i])
    i+=1
    
print('')

tu=(1,2,3,4,5,6,2)
print(tu.index(1))
print(tu.count(2))