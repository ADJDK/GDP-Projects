def midfunction(num):
    return lambda x:x+num

result=midfunction(6)

print(result(10))

number=[2,3,6,10,16,7,9,1]

filterlist=list(map(lambda x:x%2,number))

print(filterlist)
