a=int(input('enter the no to check if it div by 2 or 3 or 5:'))
if a%2==0:
    print(a,'is divisible by 2')
elif a%3==0:
    print(a,'is divisible by 3')
elif a%5==0:
    print(a,'is divisible by 5')
else:
    print('the number is not divisible by 2,3,5')
