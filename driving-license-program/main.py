print('This is the driving license program')
name=input('hi, Could you pls enter your name:')
print('Hi,',name,'Welcome to the driving license program')
age=int(input('please enter your age as well to check your eligibility for the program:'))
if age>=18 and age<60:
    print('Wonderful, you are eligible for the program')
elif age<18 and age>0:
    print('oh, I am sorry but you are not eligible for the program')
else:
    print('please enter the correct information to proceed')