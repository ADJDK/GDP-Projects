passw=input('enter the password: ')
l=u=w=s=0
for i in passw:
    if len(passw)>=8:
        l+=1
    elif i.isupper():
        u+=1
    elif i.islower():
        w+=1    
    elif i.isalnum!=True and i==' ':
        s+=1
print(l)
print(u)
print(w)
print(s)