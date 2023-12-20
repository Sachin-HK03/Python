'''for i in range(1,11):
    print(i,end=" ")
    print()'''

# conditional statemnt
'''input =int(input())
if (input>0):
    print("the given number is positive")
elif(input<0):
    print("the given number is negative")
else:
    print("the number is equals to 0")'''

# looping and conditional
i=0
'''while(i<=20):
    if(i%2==0):
        print("even numbers are:",i,"\n" ,end=" ")
    i=i+1'''

#function
'''def add(num1,num2):
    return num1+num2
print(add(30,20))
#sum=add(20,40)
#print(sum)'''

#looping and function
'''def add(list):
    listA = 0
    for i in range(len(A)):
        listA =listA+list[i]
    return listA
A=[3,2,5,4]
sum1=add(A)
print(sum1)'''

#looping and conditional and function
'''def fact(value):
    if (value == 0 or value == 1):
        return value
    else:
        value =value*fact(value-1)
    return value
factorial=int(input())
factorial1=fact(factorial)
print(factorial1)'''

#looping conditional ,function
'''def large_and_small(list):
    large=list[0]
    small=list[0]
    for i in range(len(list)):
        if list[i]>large:
            large=list[i]
        if list[i]<small:
            small=list[i]
    print(large)
    print(small)
list =[4,3,6,8]
large_and_small(list)'''

#8
'''vowels=['a','e','i','o','u']
vowels.insert(3,'9')
print(vowels)
def stng(input_str):
    vowels=['a','e','i','o','u']
    count = 0
    #input_str=''.join(list(set(list(input_str))))
    list1=[]
    for user in range(len(input_str)):
        #user =input[i]
        if input_str[user] in vowels:
            list1.append(input_str[user])
            #count +=1
    #return count
    return len(set(list1))
strings=input()
value =stng(strings)
print(value)
'''
#9
'''def simpleClaci(num1,num2,operator):
    for i in range(len(operator)):
        if operator[i] == '-':
            # print(num1-num2)
            value1=num1 - num2
        elif operator[i] =='+':
            # print(num1+num2)
            value2 = num1 + num2
        elif operator[i] =='*':
            # print(num1*num2)
            value3 = num1 * num2
        elif operator[i] =='/':
            # print(num1/num2)
            value4 = num1 / num2
            print(value1,value2,value3,value4)
input1=int(input())
input2=int(input())
operator=['+','-','*','/']
simpleClaci(input1,input2,operator)'''

#10

def strings(strng):
    long=strng[0]
    short=strng[0]
    for i in range(len(strng)):
        if len(strng[i])>len(long):
            long=strng[i]
        if len(strng[i])<len(short):
            short=strng[i]
    print(long,short)
input=["sachin","ram","killer","raghu"]
strings(input)












