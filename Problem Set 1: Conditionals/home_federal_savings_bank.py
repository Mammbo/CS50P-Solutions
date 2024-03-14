greeting = input("Greeting: ")
new_greeting = greeting.lower()
if new_greeting == "hello":
    print("$0")
elif "h" in new_greeting[0]:
    print("$20")
else:
    print("$100")