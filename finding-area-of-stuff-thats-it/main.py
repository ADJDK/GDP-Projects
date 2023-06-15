print('enter 1 to find area of rectangle.')
print('enter 2 to find area of square.')
print('enter 3 to find area of triangle.')
print('enter 4 to find area of trapezium.')
print('enter 5 to find area of circle.')
print('enter 6 to find area of semicircle.')
print('enter 7 to find area of paralellogram.')
print('enter 8 to find area of roumbus.')
print('enter 9 to find area of kite.')
print('')
a=int(input('enter the which one area you want to find:'))
if a==1:
    l=float(input('enter the length:'))
    b=float(input('enter the breath:'))
    area=l*b
    print('the area is',area)
elif a==2:
    l=float(input('enter the length:'))
    area=l*l
    print('the area is',area)
elif a==3:
    l=float(input('enter the length:'))
    b=float(input('enter the breath:'))
    area=1/2*(l*b)
    print('the area is',area)
elif a==4:
    l=float(input('enter the length:'))
    b=float(input('enter the breath:'))
    h=float(input('enter the height'))
    area=(l*b/2)*h
    print('the area is',area)
elif a==5:
    r=float(input('enter the radius:'))
    area=(r**2)*(3.14)
    print('the area is',area)
elif a==6:
    r=float(input('enter the radius:'))
    area=((r**2)*(3.14))/2
    print('the area is',area)
elif a==7:
    l=float(input('enter the length:'))
    b=float(input('enter the breath:'))
    area=l*b
    print('the area is',area)
elif a==8:
    l=float(input('enter the length:'))
    b=float(input('enter the breath:'))
    area=l*b/2
    print('the area is',area)
elif a==9:
    l=float(input('enter the length:'))
    b=float(input('enter the breath:'))
    area=l*b/2
    print('the area is',area)
else:
    print('enter the no which is provided')