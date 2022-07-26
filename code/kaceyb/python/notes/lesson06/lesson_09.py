# FIRST PIECE #

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# bruce = User('criticbruce', 'cd@email.com')

# print(bruce.username)

#      SECOND PIECE    #

import math


def distance(p1, p2):
    dx = p1["x"] - p2["x"]
    dy = p1["y"] - p2["y"]
    return math.sqrt(dx * dx + dy * dy)


p1 = {"x": 5, "y": 2}
p2 = {"x": 8, "y": 4}
print(distance(p1, p2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)


p1 = Point(5, 2)  # call the initializer, instantiate the class

p1 = (5, 2)
p2 = Point(8, 4)

# print(p1.x)
# print(p1.y)
print(type(p1))
# print(p1.distance(p2))

name = [1, 2, 3]
print(type(name))
print(name.sort())

number = input("What's your favorite number?: ")
print(type(number))
