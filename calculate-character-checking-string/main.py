st=input('enter the string')
a=str(st)
u=0
l=0
d=0
s=0
for i in a:
    if i.isupper()==True:
        u+=1
    elif i.islower()==True:
        l+=1
    elif i.isdigit()==True:
        d+=1
    elif i==" " or i.isalnum()!=True:
        s+=1
print('No of uppercase are',u)
print('No of lowercase are',l)
print('No of digits are',d)
print('No of special characters are',s)