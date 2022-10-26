## Exercise 4: Deli :ballot_box_with_check:
sandwich_orders = ["club","smoked turkey", "chicken tikka", "roast beef","tuna"]
finished_sandwiches = []

while sandwich_orders:

    current_sandwich = sandwich_orders.pop()
    print("I'm making your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I'm done making " + sandwich + " sandwich.")
