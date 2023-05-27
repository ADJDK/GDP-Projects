num=int(input('enter the no to check if it is prime or not:'))
for i in range(2,num):
    if num%i==0:
        print('it is a not prime no')
        break
else:
    print('it is a prime no')
#for prime number to check if it is prime. that number should not be divisible by any other no,
#if it is divisible then it is not prime