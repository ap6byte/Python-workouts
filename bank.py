name=input()
acc_no=int(input())
withdraw=float(input())
amount=20000
if amount<1000:
    print("Insufficient amount")
else:
    amount=amount-withdraw
    print(amount)
