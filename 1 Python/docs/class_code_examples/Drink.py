# methods:
#   -drinks should be able to be sipped
#   -drinks should be able to be refilled

# DRY
# Don't Repeat Yourself


class Drink:
    def __init__(self, owner, cup_volume):
        self.volume = 0
        self.cup_volume = cup_volume
        self.owner = owner

    def whose_drink(self):
        return f'this drink belongs to {self.owner}'

    def sip_drink(self, size):
        # lower drink's volume by some small amount
        if size == 'gulp':
            self.volume -= 2.5
        elif size == 'chug':
            self.volume -= self.volume
        else:
            self.volume -= .1
        return self.volume

    def refill(self):
        self.volume += self.cup_volume


class Seltzer(Drink):
    def __init__(self, owner, cup_volume, flavor):
        super().__init__(owner, cup_volume)
        self.flavor = flavor

seltzie = Seltzer('sarah', 12, 'apple')
print(seltzie)

# drink = Drink(12, 'Zach')
# print(drink.volume) #0
# drink.refill()
# print(drink.volume) #12


# drank = Drink(24, 'Ozz')
# print(drink.whose_drink())
# print(drink.sip_drink('chug'))

# while True:
#     order = input('What would you like to drink? ')
#     name = input('whats your name? ')
#     size = float(input('what size cup do you want? Enter ounces in number: '))

#     drink = Drink(name, size)
#     drink.refill()
#     print(f'Here is your {order}')


# create a class SpecificTypeOfDrink(class choice)
# should inherit from class Drink

