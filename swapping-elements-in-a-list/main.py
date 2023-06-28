lst=[1,2,3,4,5,6,7,8,9]
print(len(lst))
t=lst[0]
lst[0]=lst[len(lst)-1]
lst[len(lst)-1]=t
print(lst)