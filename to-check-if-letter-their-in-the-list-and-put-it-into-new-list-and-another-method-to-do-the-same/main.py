lst=['lion','elephant','tiger','monkey','donkey']
newlst=[]
for i in lst:
    if 'e' in i:
        newlst.append(i)
print(newlst)


lst=['lion','elephant','tiger','monkey','donkey']
newlst=[i for i in lst if 'e' in i]                                 #different method to access elements for list
print(newlst)