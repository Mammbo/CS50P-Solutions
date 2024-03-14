light = 300000000

def einstein(mass):
    energy = mass * light ** 2
    print(f"Energy: {energy}")

mass =  int(input("What is the mass of your object in Kg's: "))
einstein(mass)