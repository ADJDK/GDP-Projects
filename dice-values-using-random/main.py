min=1
max=6
import random
import time
roll='yes'
while roll=='yes' or roll=='y':
    print('rolling the dice...')
    time.sleep(1)
    print('the values is')
    dic=random.randint(min,max)
    print(dic)
    roll=input('wanna roll again:')
else:
    print('exit')
