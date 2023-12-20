num=int(input())
n1,n2=0,1
count=0
if num<=0:
    print("enter the positive number")
elif num == 1:
    print("fib equence upto,",num)
else:
    while count<num:
        # print(n1)
        temp=n2
        n1=n1+n2
        n2=n1
        count +=1
print(n1)