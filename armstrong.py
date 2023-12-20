number = int(input())
temp=number
sum=0
while temp>0:
    digit=temp%10
    sum =sum+digit **3
    #print(sum)
    temp=temp//10
if sum==number:
    print("armstrong")
else:
    print("not a armstrong")