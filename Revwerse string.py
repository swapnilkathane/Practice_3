def revers (s):
    words=s.split()
    length=len(words)
    #print(length)
    list=[]
    spl=" "
    n=0
    while(n<length):
        for x in words:
            list.insert(0,x)
            n+=1
    #print(list)
    rev=0
    g=len(list)
    #print(g)
    n1=0
    while(n1<g):
        for x in list:
            rev=spl + " " +list[n1]
            spl=rev
            n1+=1
    return rev

name=input('Enter the string to reverse : ')
print(revers(name))
