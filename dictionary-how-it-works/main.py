d={'car':'the thing which moves','bus':'the big thing which moves','bike':'the small thing which moves',
    1:'one',
    2:3,
    'bright':['light','night']
    
}
print(d)
print('the element accessed here',d['bright'])

d1={1:'one',2:'two',3:'third',3:'three',4:'four',5:'five'}  #see no duplicate values
print(d1)
print(len(d1))
print(type(d1))
print(d1.keys())
print(d1.values())
print(d1.get(3))
d1[4]='zero'
print(d1)