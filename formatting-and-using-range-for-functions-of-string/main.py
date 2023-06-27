A='greeting to you all'
print(A.endswith('all',0,len(A)))
print(A.find('to',0,len(A)))
print(A.index('you',0,len(A)))
print('greeting to {} {}'.format('you','all'))
print('greeting to {1} {0}'.format('you','all'))
print('greeting to {b} {a}'.format(a='you',b='all'))


t=('my','class','you','all')
print('see {} {}'.format(t[0],t[1]))


d={'my':'sql','class':'book'}
print('welcome to {} {}'.format(d['my'],d['class']))


tup=('my','name','is','adrik')
a='#'.join(tup)                                                 #for collection of things we use opposite of normal
                                                                #join
print(a)

d={'nice':'place','car':'home'}
j='*'
w=j.join(d)
print(w)