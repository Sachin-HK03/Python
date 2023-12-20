N=int(input())
input=[int(x) for x in input().split(' ')]
l_digit=[]
for i in range (N):
    last=input[i]
    l_digit.append(last%10)
    print(l_digit)
if l_digit[-1] == 0:
    print('Yes')
else:
    print('No')



