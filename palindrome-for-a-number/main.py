num=input('enter the no:')
reverse=0
length=len(num)
num=int(num)
temp=num
for i in range(length):
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10
print('the original no is',temp)
print('the reverse no is',reverse)
if temp==reverse:
    print('it is a palindrome')
else:
    print('it is not a palindrome')