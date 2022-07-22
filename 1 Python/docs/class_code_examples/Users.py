class User:
    species = 'human'
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __str__(self):
        return self.username

class SuperUser(User):
    def __init__(self, username, email):
      super().__init__(username, email)



bruce = SuperUser('criticbruce', 'cb@email.com')
print(bruce.species)
Kacey = User('demo', 'demo@email.com')
print(Kacey.species)
print(type(bruce))
print(bruce)



# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     @staticmethod
#     def circumference(self, radius):
#         c = 2 * self.pi * radius
#         return Circle(c)

# egg = Circle(6)
# print(egg.circumference(egg.radius))


# def distance(p1, p2):
#     dx = p1['x'] - p2['x']
#     dy = p1['y'] - p2['y']
#     return math.sqrt(dx*dx + dy*dy)

# p1 = {'x': 5, 'y': 2}
# p2 = {'x': 8, 'y': 4}
# print(distance(p1, p2))

class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

# p1 = Point(5, 2) # call the initializer, instantiate the class

# p1 = (5,2)
# p2 = Point(8, 4)

# # print(p1.x) # 5
# # print(p1.y) # 2
# print(type(p1)) # Point
# print(p1.distance(p2))





import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

# p3 = Point()
# p2 = Point(8,4)
# dist = p1.distance(p2) # or p2.distance(p1), either works
# print(dist)