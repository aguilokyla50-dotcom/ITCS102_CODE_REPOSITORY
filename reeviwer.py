age = int(input("Your age--->"))
rev = float(input("your monthly revenue--->"))
cs = int(input("Your credit score--->"))
yib = float(input("Years in bussiness"))
hd = bool(input("Has defaults?--->"))
cn = str(input("Collateral name---."))
cv = float(input("Collateral value--->"))

#baseline age>= 21, yrs > 2.0, dont have aany default

max_loan = 0 
base_fee = 0

if age >= 21 and yrs >= 2.0 and hd == False:
    print("BASELINE CRITERIA PASSED")
    if cs >= 720: # tier 1
        max_loan = rev * 3
        print("MAXIMUM AMOUNT THAT CAN BE LOAN IS SET TO",max_loan)
        print ("HIGH CREDIT SCORE")
        if rev >= 50000:
            print("REVENUE HIGHER THAN 50K ")
            base_fee = max_loan * 0.015
            print("BASE FEE RATE IS SET TO ", base_fee)
        else:
            print("REVENUE LOWER THAN 50K")
            base_fee = max_loan * 0.025
            print("BASE FEE RATE IS SET TO"base_)

    elif cs >= 620 and cs < 720: # tier 2
        print(" credit score within the range of 620 to 720")

    
    else:
        print("INVALID")
else:
    print("baseline failed")
    