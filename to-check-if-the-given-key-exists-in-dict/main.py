d={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nice'}
k=int(input('enter the key which value you want to get:'))
if k in d:
    print('the given keys value is',d[k])
else:
    print('the key doesnt exist in the dict')