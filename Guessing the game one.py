import random
n=0
while(n<=3):
    num1=int(input('Guess any number between 1-9: '))
    num2=random.randrange(1,9)
    print(num2)
    if(num1-num2>2): print("too high")
    if(num1-num2<=2): print('too low')
    if(num1==num2): print('equal')
    n+=1
