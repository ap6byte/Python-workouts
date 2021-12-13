unit=float(input("Enter number of units consumed: "))
if unit<=100:
    print("No Payment due")
elif unit>100 and unit<200:
    amount=(unit-100)*5
    print("Payment due for ",unit,"consumed is",amount)
else:
    amount=500+(unit-200)*20
    print("Payment due for ",unit,"consumed is",amount)
