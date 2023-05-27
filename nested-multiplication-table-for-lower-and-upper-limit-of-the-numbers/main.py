lower=int(input('enter the lower limit'))
upper=int(input('enter the upper limit'))
for i in range(lower,upper+1):
    for j in range(1,11):
        print(i*j,end=' ')
    print()