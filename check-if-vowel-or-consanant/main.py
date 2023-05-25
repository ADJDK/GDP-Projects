a=input('enter the alphabets to check if it is vowels or consonant:')
if a in ['a','e','i','o','u'] and len(a)==1:
    print('it is a vowel')
elif a not in ['a','e','i','o','u'] and len(a)==1:
    print('it is a consonant')
else:
    print('pls enter the correct input')
