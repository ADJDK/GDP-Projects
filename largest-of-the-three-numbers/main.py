a=int(input('enter the first no:'))
b=int(input('enter the second no:'))
c=int(input('enter the third no:'))
if a>b and a>c:
    print(a,'is the largest no')
elif b>a and b>c:
    print(c,'is the largest no')
else:
    print(c,'is the largest no')
