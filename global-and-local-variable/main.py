greet='welcome'                    #can be used outside and inside the function                                            

def wel():
    print(greet,'to the world young one')

wel()
print(greet,'the people')

#----------------------------------------------------------------------------

greeting='super'

def top():
    greet='cars'
    print('i love',greet)

top()

print(greeting,'man')

#----------------------------------------------------------------------------

def gl():
    global part                                             #first make the thing global then only we can 
    part='the world is the best'                            #use it otherwise error    
    print(part)

gl()
print(part)