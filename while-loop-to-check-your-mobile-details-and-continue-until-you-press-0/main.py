cho=1
while cho!=0:
    print('press 1 to check balance')
    print('press 2 to check validity')
    print('press 3 to check package')
    print('press 0 to exit')
    cho=int(input(''))
    if cho==1:
        print('your balance is 100$')
    elif cho==2:
        print('your validity is still 1/3/2024')
    elif cho==3:
        print('your package is for unlimited calls')
    else:
        break