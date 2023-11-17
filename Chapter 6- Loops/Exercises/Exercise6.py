beer_orders = ["Red horse","San Miguel", "Emperador", "Tanduay","Black Label"]
finished_orders = []

while beer_orders:

    current_beer = beer_orders.pop()
    print("I'm making your " + current_beer + ".")
    finished_orders.append(current_beer)

print("\n")
for beer in finished_orders:
    print("I'm done making your " + beer + " come take it.")

