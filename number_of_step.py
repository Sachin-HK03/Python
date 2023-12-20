def sub(a,b,n):
    new_arr=[]
    for x,y in zip(a,b):
        new_arr.append(x-y)
    a=new_arr
    f=0
    for x1 in a:
        if x1<0:
            f=1
    if f==0:
        return 1+sub(a,b,n)
    else:
        return 0
        """ 
        if a>b:
            new1=a-b
            new.append(new1)
            count+=1
            sub(a,b)
        print(count)
        
    else :
            print(-1)
            """

count=0
n=int (input())
"""
a=[]
b=[]

for i in range(n):
    ele=int(input())
    a.append(ele)
    print(a)
for i in range(n):
    ele = int(input())
    b.append(ele)
    print(b)
"""
a=[int(x) for x in input().split(' ')]
b=[int(x) for x in input().split(' ')]
ls=sub(a,b,n)
print(ls+1)