value = 50
while value > 0:
    print("Amount Due: ",value)
    coin=int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        value -= coin
    else:
        print("Wrong denomination!")
else: 
    print("Change owed: ",abs(value))
    
