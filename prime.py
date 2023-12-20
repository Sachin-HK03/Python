n=int(input())
if n==1:
    print("not a prime number")
elif n>1:
    for i in range (2,(n//2)+1):
        if (n%i) == 0:
            print("its not prime number")
            break;
    else:
        print("its a prime number")
else:
    print("not a prime..")