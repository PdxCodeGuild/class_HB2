class CleanDish:
    def __init__(self, cleanliness, color):
        cleanliness = self.cleanliness
        color = self.color


class DirtyDish:
    def __init__(self, cleanliness, color):
        cleanliness = self.cleanliness
        color = self.color

class Clild(CleanDish, DirtyDish):
    def __init__(self):
        CleanDishes.__init__(self)
        DirtyDishes.__init__(self)