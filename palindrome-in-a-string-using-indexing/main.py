st=input('enter the word to check if it is palindrom or not: ')
a=st[::-1]
print('the reverse of it is',a)
if st==a:
    print('it is a palindrome')
else:
    print('it is not a palindrome')