## Exercise 1: Pizza Toppings

prompts = "\nWhat do you want in your pizza?"
prompts += "Enter 'quit' when your done:"

while True:

    topping = input(prompts)
    if topping != 'quit':
        print("I'll add " + topping + " to your pizza.")
    else:
        break
    