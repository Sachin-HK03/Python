def sub(a,b,n):
    new_arr=[];
    for x in range(n):
        global count
        if a[x]>b[x]:
            new_arr.append(a[x]-b[x])
            a=new_arr;
            count +=1;
            sub(a,b,n)
    print(a,count)

n=int (input())
count=0;
a=[int(x) for x in input().split(' ')]
b=[int(x) for x in input().split(' ')]
ls=sub(a,b,n)