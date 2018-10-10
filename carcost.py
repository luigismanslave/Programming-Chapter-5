def cars():
    loan = float(input('Enter the monthly cost of the loan payment:'))
    insur = float(input('Enter the monthly cost of the insurance payment:'))
    gas = float(input('Enter the monthly cost of gas:'))
    oil = float(input('Enter the monthly cost of oil:'))
    tire = float(input('Enter the monthly cost of tires:'))
    maint = float(input('Enter the monthly cost of maintenance:'))
    totalm = loan + insur + gas + oil + tire + maint
    totaly = totalm * 12
    print("Your total monthly cost for your car is $", totalm, "and the yearly cost is $", totaly)
    return totaly, totalm
cars()
