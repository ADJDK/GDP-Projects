y=lambda x:x*10         #parameter        #x is used to store the variable
                                        #after : this the whatever function we need to perform we do it
print(y(5))           #argument       # lambda is basically like a function just be different


z=lambda m,n,o:m*n*o
                        #lambda will store the assigned values to the variable just like the return function
print(z(1,2,3))

#----------------------------------------------------------------------------------------------------------------

def miscount(num):
    return lambda x:x*num
    
result=miscount(3)

print(result(3))