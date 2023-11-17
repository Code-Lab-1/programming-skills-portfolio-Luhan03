prompts = "\nWhat do you want to order? "
prompts += "Enter 'quit' when your done:"

while True:

    order = input(prompts)
    if order != 'quit':
        print("I'll add " + order + " to your basket.")
    else:
        break