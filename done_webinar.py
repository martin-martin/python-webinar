# PACKAGES
# pip uninstall --no-cache-dir -y -r <(pip freeze)
# pip install requests
import requests


response = requests.get("https://raw.githubusercontent.com/martin-martin/pizza-pie/master/recipe.txt")
# print(response.text)
recipe = response.text
lines = recipe.split('\n')
# print(lines)

# ---------------------------------------------------------------------------

# DATATYPES: LISTS
ingredients = []
# FOR LOOP
for line in lines:
    ing = line.split()
    ingredients.append(ing)

# show example of datatypes, operators, and conditionals in interpreter

# ---------------------------------------------------------------------------


# FUNCTIONS, ARGUMENTS
def mash(ing_1, ing_2):
    new_amount = ing_1[0] + ing_2[0]
    print(f"you mash and receive {new_amount} ... things...?")
    print(f"Ok, let's call them yummy '{ing_1[1] + ing_2[1]}'")
    return new_amount


# potentially redo this content with the Ingredient class!! (time!)
mash(ingredients[2], ingredients[-1])

# ---------------------------------------------------------------------------

# DATATYPES: DICTIONARIES
ing_dict = {}
for ing in ingredients:
    name = ing[1]
    # TYPE CONVERSION
    amount = int(ing[0])
    ing_dict[name] = amount

print(ing_dict)

ing_dict.pop('olive_oil')
ing_dict.pop('garlic_cloves')

for key, value in ing_dict.items():
    ing_dict[key] = value * 2

print(ing_dict)

# ---------------------------------------------------------------------------

# FILE OUTPUT
with open('new_recipe.txt', 'w') as f_out:
    recipe = "IMPROVED RECIPE\n\n"
    for name, amount in ing_dict.items():
        recipe += f'{amount} {name}\n'
    f_out.write(recipe)

