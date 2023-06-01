print('welcome to bright champs')
print('to check whether your internet speed is good or bad')
internet=int(input('enter your internet speed:'))
while internet>0:
    if internet>=50:
        print('your internet speed is fantastic')
        print('you can attend the class')
        break
    elif internet<50 and internet>=25:
        print('your internet is good ')
        print('you can attend the class')
        break
    elif internet<25 and internet>=10:
        print('your internet is okay ')
        print('you can attend the class')
        break
    elif internet<10 and internet>=1:
        print('hm your internet speed doesnt look that good')
        print('you can not attend the class')
        break
else:
    print('pls check your internet speed and you can attend the class')