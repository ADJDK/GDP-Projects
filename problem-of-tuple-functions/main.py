t1=(1,2,3,4)
t2=(5,6,7,8,2)
t=t1+t2
print(t)
print('')
print(t[-2])
print('')
print(t.count(2))
print('')
for i in t:
    if i%2==0:
        print(i)