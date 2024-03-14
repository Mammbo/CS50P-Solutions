coke = 50 
while coke != 0: 
    print(f"Amount Due: {coke}")
    user = int(input("Insert Coin: "))
    if user == 25 or user == 10 or user == 5: 
        coke = coke - user 
    else: 
        continue 
    if coke != 0: 
        continue 
    else: 
        print("Change Owed: 0")