## Exercise 3: Infinity
prompt = "How old are you?"
prompt += "Enter 'quit' when you're done."

while True:

    age = input("How old are you?")
    
    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age < 13:
        print("You have to pay $10")
    else:
        print("You have to pay $15")
