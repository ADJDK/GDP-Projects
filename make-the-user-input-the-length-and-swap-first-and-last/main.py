lst=[1,2,3,4,5,6,7,8,9]
print(lst)
a=int(input('now find the length of the list:'))
if a==len(lst):
    print('yes that is the length of the list ')
else:
    print('no that is not the correct length')
t=lst[0]
lst[0]=lst[len(lst)-1]
lst[len(lst)-1]=t 
print(lst)