q='yes'
while q=='yes':
    num=int(input('enter the no'))
    if num%2==0:
        print('it is an even no')
        break
    else:
        print('it is odd no')
        break
    q=input('do you wanna try once more (yes or no)')
print('quit')