import random
rol='yes'
while rol=='yes':
    print('rolling the dice...')
    print('the value is')
    dic=random.randint(1,6)
    print(dic)
    dic1=random.randint(1,6)
    print('the total is',dic+dic1)
    rol=input('do you wanna do it again: ')
    print('')
else:
    print("exit")
