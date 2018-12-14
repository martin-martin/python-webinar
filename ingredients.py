class Ingredient:

    # INITIALIZATION METHOD
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    # METHODS
    def use(self, use_amount):
        self.amount -= use_amount

    # CUSTOM DUNDER STRING
    def __str__(self):
        return f"there are {self.amount} of {self.name}."