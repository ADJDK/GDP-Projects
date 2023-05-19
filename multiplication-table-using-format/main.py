print('welcome to multiplication chat bot')
print('enter the no of which you want multiplication table of')
num=int(input())
for i in range(1,11):
    print('{} x {} = {}'.format(num,i,(num*i)))
