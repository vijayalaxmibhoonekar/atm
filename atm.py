balance=5000
print("welcome to icici atm")
pin=(input("enter pin number:"))
if pin=="5763":
    amt=int(input("enter amount:"))
    if(amt%100)==0:
       if amt<=20000:
         if amt<=balance:
            balance=balance-amt
            print("available balance:",balance)
         else:
            print("no funds")
       else:
            print("no limit")

    else:
        print(" enter valid amount:")
else:
  print("invalid pin")
print("thanks for using atm")




