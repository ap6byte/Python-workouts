amt=float(input("Enter the price of your bike:"))
if amt>100000:
    print("Road tax:",(.15*amt))
elif amt<=100000 and amt>50000:
    print("Road tax:",(.1*amt))
elif amt<=50000:
    print("Road tax:",(.05*amt))
