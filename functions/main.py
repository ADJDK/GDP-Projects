def lengths():
    a=input('enter the string whose length you wanna find: ')
    print('the lenght is',len(a))


def ab():
    st=input('enter the word:')
    s=input('enter the first two letters of the word:')
    t=input('enter the last two letters of the word:')
    print('')
    if st.startswith(s) and st.endswith(t):
        print('Yes it is correct, here is the word',st)
    else:
        print('nope, wrong print the word again')

def swap():
    st=input('enter the first string')
    stri=input('enter teh second string')
    new=st[:2]+stri[2:]
    new1=stri[:2]+st[2:]
    print(new + new1)
swap()
