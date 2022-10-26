## Exercise 5: No Pastrami

sandwich_orders = ["club","pastrami","smoked turkey", "pastrami","chicken tikka", "roast beef","pastrami","tuna"]
finished_sandwiches = []

print("\nSorry, we dont have pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm making your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I'm done making " + sandwich + " sandwich.")
    