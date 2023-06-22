import random
num=random.randint(1,10)
chance=5
while chance>0:
    num1=int(input('guess a number between 1 and 10:'))
    if num==num1:
        print('you guessed it correct')
        break
    else:
        print('you guessed it wrong')
    chance-=1
    print('the number of chance left are',chance)
    print('\n')
else:
    print('the actual no was',num)