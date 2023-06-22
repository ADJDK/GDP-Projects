import random
print('rock,paper,scissor')
play=input('your choice:')
randnum=random.randint(1,3)
if randnum==1:
    comp='rock'
elif randnum==2:
    comp='paper'
elif randnum==3:
    comp='scissor'
print('computer choice:',comp)

if comp==play:
    print('it is tie')
elif comp=='paper':
    if play=='rock':
        print('paper defeats rock, hence lose')
    elif play=='scissor':
        print('scissor defeats paper')
elif comp=='rock':
    if play=='scissor':
        print('scissor loses rock, hence won')
    elif play=='paper':
        print('paper deafeats rock')
elif comp=='scissor':
    if play=='rock':
        print('rock deafeats scissors, hence lose')
    elif play=='paper':
        print('scissor defeats paper')


