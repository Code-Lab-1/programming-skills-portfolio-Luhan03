## Exercise 2: Movie Tickets:

prompt = "How old are you?"
prompt += "Enter 'quit' when you're done."

while True:
    age = input(prompt)

    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free")
    elif age < 13:
        print("You have to pay $10")
    else:
        print("You have to pay $15")
