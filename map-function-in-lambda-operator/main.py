number_list=[2,4,6,10,12,16,3,24,19,36]

filtered_list=list(map(lambda num:num%4,number_list))

print(filtered_list)


#so basically map will give the result for everything in the list unlike filter which will remove all the 
#unwanted elements from the list and only give the needed results