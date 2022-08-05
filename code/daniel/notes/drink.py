class Drink:
    def __init__(self, volume, owner, cup_volume):
        self.volume = cup_volume
        self.cup_volume = cup_volume
        self.owner = owner

    def whose_drink(self):
        return f'This drink belongs to {self.owner}'

    def sip_drink(self, size):
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

seltzer = Seltzer(Drink)
print(seltzer)


# drink = Drink(12, 'Zach')
# print(drink.volume)
# drink.refill()
# print(drink.volume)


# drank = Drink(24, 'Ozz')
# print(drink.whose_drink())
# print({drink.sip_drink('chug')})


# while True:
#     order = input('What would you like to drink?')
#     name = input('What is your name?')
#     size = input('What size cup do you want?')

#     drink = Drink(name, size)
#     drink.refill()
#     print('Here is your {order}')

