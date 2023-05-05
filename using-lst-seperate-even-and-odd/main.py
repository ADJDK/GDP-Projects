lst=[1,2,3,4,5,6,7,8,9]
lst_even=[]
lst_odd=[]
for i in range(9):
    if lst[i]%2==0:
        lst_even.append(lst[i])
    else:
        lst_odd.append(lst[i])
print(lst_even)
print(lst_odd)