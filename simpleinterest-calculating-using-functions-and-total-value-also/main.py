def simint(p,t,r=10):
    si=(p*t*r)/100
    print('the simple intereset is',si)
    return si

def total(p,si):
    return p+si
    

p=int(input('enter principal'))
t=int(input('enter the time'))
r=int(input('enter the rate'))

si=simint(p,t,r) 



print(total(p,si))

