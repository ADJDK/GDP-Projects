nest=[[1,2,3],[4,5,6],[7,8,9]]
count=0
sum=0
for sub in nest:
    for i in sub:
        count+=1
        sum+=1
print('the sum is',sum)
print('the no of elements is',count)
average=sum/count
print('the average of the elements in the list is',int(average))