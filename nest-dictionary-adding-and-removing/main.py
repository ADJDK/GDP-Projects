stu={1:{'name':'adrik','class':12},2:{'name':'dam','class':'5'}}
print(stu)
stu.update({3:{'name':'rihik','class':3},4:{'name':'mohit','class':7}})
print(stu)
stu.popitem()
print(stu)
stu[1]['class']=20
print(stu)
for i in stu.values():
    print(i)