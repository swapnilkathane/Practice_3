def fibo (num):
    prev=0
    curr=1
    l=[]
    l.append(curr)
    a=0
    while(a<num-1):
        nxt=prev+curr
        prev=curr
        curr=nxt
        l.append(nxt)
        a+=1
    return l


term=int(input('Enter how much terms do you want ? '))
print(fibo(term))