op=int(input('enter 1 if you want to add. \nenter 2 if you want to sub.\nenter 3 if you want to mul. \nenter 4 if you want to div.'))
a=int(input('enter the first no:'))
b=int(input('enter the second no:'))
if op==1:
    print('the addition of these two no is',a+b)
elif op==2:
    print('the substraction of these two no is',a-b)
elif op==3:
    print('the multiplicaiton of these two no is',a*b)
elif op==4:
    print('the division of these two no is',a/b)
else:
    print('pls enter the number asked above')