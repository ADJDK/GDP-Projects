def surfacearea(r):
    print('the surface area is:')
    return 4*3.14*r**2

def volumerofsphere(r):
    print('the volume of sphere is:')
    return 4/3*3.14*r**3

def diameter(r):
    print('the diameter is:')
    return r*2
    
    
def radius(r):
    print('the radius is')
    return r
    
rad=int(input('enter the radius:'))
s=surfacearea(rad)
v=volumerofsphere(rad)
d=diameter(rad)


print(s)
print(v)
print(d)