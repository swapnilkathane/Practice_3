name=input('Enter the name of list ')
num=int(input('How many elements doy ou want in list ? '))
b=str(name)
c=[]
while(num>0):
    d=int(input('Enter element '))
    c.append(d)
    num=num-1
print(b, '=',c)