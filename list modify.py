L1=[1,2,3,4,5,5,6]
b=len(L1)
n=0
L2=[]
while(n<b):
    for x in L1:
        if x in L2:
            #m=1 #to print duplicate elements only once
            L2.remove(x) #to remove the duplicate elements in list
        else:
            L2.append(x)
        n+=1
    print(L2)



