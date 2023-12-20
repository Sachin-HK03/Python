string1=str(input())
string2=str(input())
if len(string1)!=len(string2):
    print("its not anagram")
else:
    temp1=string1.lower()
    temp2=string2.lower()
    sort1=sorted(temp1)
    sort2=sorted(temp2)
    if sort1==sort2:
        print("its anangram")
    else:
        print('its not anagram')