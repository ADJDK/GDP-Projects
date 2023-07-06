d={1:{'car':'nissan','price':10},2:{'car':'infinity','price':2}}
print('the nested dict value',d[1]['car'])
print(d[2]['price'])
for i in d.keys():
    print('these are the keys',i)
d.clear()
print(d)
del d