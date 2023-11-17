## Exercise 4: Rivers

rivers = {'Nile': "Egypt", 'Amazon':'South America','Mississippi-Missouri-Red Rock': 'United States'}

for river, country in rivers.items():
    print("The " + river + " flows through " + country + ".")

print("\nNames of each river included in the dictionary.")
for river in rivers.keys():
    print('- ' + river)

print("\nName of each country included in the dictionary.")
for country in rivers.values():
    print('-' + country)
    