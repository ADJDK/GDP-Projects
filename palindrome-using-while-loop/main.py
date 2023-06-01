num=input('enter the no:')
reverse=0
length=len(num)
num=int(num)
temp=num
while True:
    for i in range(length):
        remainder=num%10
        reverse=reverse*10+remainder
        num=num//10
    break
print('this is the reversed no:',reverse)
print('this is the original no:',temp)
if temp==reverse:
    print('it is a palindrome')
else:
    print('it is not a palindrome')

    
