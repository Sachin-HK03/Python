vowels=['A','E','I','O','U','Y']
input=input()
for input in vowels:
    print("invalid")
    break;
else:
    if input[0]+input[1] == 0:
        print("valid")