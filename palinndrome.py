string=input()
temp=[];
for i in range(1,len(string)+1):
    temp.append(string[-i])
var=''.join(temp)
if var == string:
    print("its palindrome")
else:
    print("its not a palindrome")





