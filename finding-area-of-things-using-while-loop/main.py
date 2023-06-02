r='y'
while r.lower()=='y':
    print('pls enter 1 if you want to find rectangle:')
    print('pls enter 2 if you want to find triangle:')
    print('pls enter 3 if you want to find square:')
    cho=int(input('choose any one of the three:'))
    if cho==1:
        l=int(input('enter the length:'))
        b=int(input('enter the breath:'))
        area=l*b
        print(area)
    elif cho==2:
        l=int(input('enter the length:'))
        b=int(input('enter the breath:'))
        area=1/2*l*b
        print(area)
    elif cho==3:
        l=int(input('enter the length of the side:'))
        area=l*l
        print(area)
    else:
        print('pls enter 1,2,3 only')
    r=input('do you want to do it again y/n:')
    print('exit')
    