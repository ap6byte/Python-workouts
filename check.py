ch=input("please enter any character :")
if(ch>='a' and ch<='z')or(ch>='A' and ch<='Z'):
    print("the given charcter",ch,"is an alphabet")
elif(ch>='0' and ch<='9'):
    print("the given charcter",ch,"is a digit")
else:
    print("the given charcter",ch,"is a special character")
