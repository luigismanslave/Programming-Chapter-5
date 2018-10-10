def insurance():
    amount = float(input('What is the replacement cost of the structure?:'))
    amount = amount * .8
    print('You should buy $', amount, 'worth of insurance')
    return amount
insurance()
