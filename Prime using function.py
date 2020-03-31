def prime (num):
    a=2
    p=0
    print(type(a))
    while(a<num):
        if(num%a!=0):
            b=1
        else:
            p+=1
        a+=1
    print(p)
    if(p==0):
        return 1
    else:
        return 0

i=int(input('Enter the number'))
y= prime(i)
if(y==1):
    print('Given number is prime number')
else:
    print('Given number is not prime number')
