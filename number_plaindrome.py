number= int(input())
temp=number
rem=number%10
reverse=0
while temp>0:
    rem = temp % 10
    reverse=reverse*10+rem
    temp=temp//10
if number==reverse:
    print("it is a palindrome")
else:
    print("its not a palindrome")

