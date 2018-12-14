# fetch a web resource
import requests

# VARIABLES AND VALUES
response = requests.get("https://raw.githubusercontent.com/martin-martin/pizza-pie/master/recipe.txt")

recipe = response.text

lines = recipe.split('\n')  # newline character

# LISTS
ingredients = []
# FOR LOOP
for line in lines:
    ingredient = line.split()
    ingredients.append(ingredient)

ingredients.pop(1)  # remove garlic_cloves
ingredients.pop(0)  # remove olive_oil

#print(ingredients)

ing_1 = ingredients[0]
amount_1 = ing_1[0]

ing_2 = ingredients[1]
amount_2 = ing_2[0]

# TYPE CONVERSION
num_1 = int(amount_1)
#print(type(num_1))

# FUNCTIONS


def mash(ing_1, ing_2):
    print(f"Here's some yummy {ing_1[1] + ing_2[1]}!")


#mash(ingredients[0], ingredients[1])
#mash(ingredients[0], ingredients[2])
#mash(ingredients[1], ingredients[2])


# FILE I/O
with open('new_recipe.txt', 'w') as f:
    f.write("RECIPE\n\n")
    f.write(recipe)


with open('new_recipe.txt', 'r') as f:
    new_recipe = f.read()

print(new_recipe)


#var_1 = "hello"
# var_1 ====> "hello"

# DATATYPES
# - STRINGS
# - INTEGERS
# - FLOAT
# - BOOLEANS

# OPERATORS
# - ARITHMETIC OP.
# - COMPARISON (==, >=, >, <, <=, !=)
# - LOGICAL (and, or, not)
