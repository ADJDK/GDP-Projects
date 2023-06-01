n=int(input('enter the no for the factorial'))
while n>=1:
    a=1
    for i in range(1,n+1):
        a=a*i
    print(a)
    break
else:
    print('we cant find the factorial')