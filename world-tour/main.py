print('welcome to the world tour bot.')
print('press 1 if you want to visit europe.')
print('press 2 if you want to visit asia.')
print('press 3 if you want to visit africa.')
print('press 4 if you want to visit australia')
ch=int(input('pls enter your choice:'))
if ch==1:
    state=input('In europe choose btw finland,germany,UK: ')
    if state=='finland':
        print('welcome to the country of good')
    elif state=='germany':
        print('the land of the poets')
    elif state=='UK':
        print('the land of the british')
    else:
        print('pls choose btw finland,germany,UK')
elif ch==2:
    state=input('In asia choose btw india,china,korea: ')
    if state=='india':
        print('welcome to the country of spices')
    elif state=='china':
        print('the land of the too much people')
    elif state=='korea':
        print('the land of the kpop')
    else:
        print('pls choose btw india,china,korea')
elif ch==3:
    state=input('In africa choose btw ghana,kenya,sudan: ')
    if state=='ghana':
        print('welcome to the country of the worlds most beautiful people')
    elif state=='kenya':
        print('the land of the entrepenuars')
    elif state=='sudan':
        print('the land of the the coffee')
    else:
        print('pls choose btw ghana,kenya,sudan')
elif ch==4:
    state=input('In australia choose btw new zealand,fiji,solomon: ')
    if state=='new zealand':
        print('welcome to the country of the worlds beautiful things')
    elif state=='fiji':
        print('the land of the mountains')
    elif state=='solomon':
        print('the land of the the ocean')
    else:
        print('pls choose btw new zealand,fiji,solomon')
else:
    print('pls choose btw choices 1,2,3,4')        



