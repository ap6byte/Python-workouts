name=input("Enter your name: ")
maths=float(input("Enter your maths marks: "))
english=float(input("Enter your english marks: "))
sci=float(input("Enter your science marks: "))
it=float(input("Enter your IT marks: "))
percent=(maths+english+sci+it)/2
if percent>65:
    print(name,"pass")
else:
    print(name,"fail")
