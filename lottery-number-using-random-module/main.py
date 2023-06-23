import random
a=random.randint(1,10)
chance=3
while chance>0:
    num=int(input('enter the lottery number: '))    
    if num==a:
        print('Wow, You have won the lottery') 
    else:
        print('Ops, You lost')
    chance-=1
    print('you now have only',chance,'left')
    print('')
else:
    print('you have lost the lottery')
    print('The actually lottery number was',a)