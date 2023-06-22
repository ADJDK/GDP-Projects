import random
num=random.randint(1,10)
num1=int(input('guess a no between 1 and 10:'))
if num1==num:
    print('you guessed correct')
else:
    print('you guessed wrong')
    print('the actually no was',num)