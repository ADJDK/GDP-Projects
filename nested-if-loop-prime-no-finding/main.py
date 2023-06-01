num=int(input('enter the no to check if prime or not:'))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print('it is not a prime no')
    else:
        print('it is a prime no')
else:
    print('it is not a prime no')
            