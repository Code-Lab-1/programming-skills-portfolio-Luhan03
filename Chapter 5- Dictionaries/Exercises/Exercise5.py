## Exercise 5: Pets
pets = []

pet = {'animal type':'Cat','name':'Klai','owner':'Von'}
pets.append(pet)

pet = {'animal type':'Dog','name':'Fluffy','owner':'Dianne'}
pets.append(pet)

pet = {'animal type':'Cat','name':'Elle','owner':'Von'}
pets.append(pet)

for pet in pets:
    print("\nHere is some of the info that I know about " + pet['name'] + ":")
    for key, value in pet.items():
        print(key + ": " + str(value))
        