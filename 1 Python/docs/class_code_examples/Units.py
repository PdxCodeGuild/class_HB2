number = 0 #does not influence 'number' inside class

class Distance:

    def __init__(self, number, unit):
        self.number = number
        self.unit = unit

    def to_meters(self):
        if self.unit == 'm':  # meters
            return self.number
        elif self.unit == 'miles': # miles
            return self.number * 1609.34
        elif self.unit == 'ft': # feet
            return self.number * 0.3048
        elif self.unit == 'km': # kilometers
            return self.number * 1000
        elif self.unit == 'yd': # yards
            return self.number * 0.9144
        elif self.unit == 'in': # inches
            return self.number * 0.0254

to_portland = Distance(3000, 'miles')

to_portland.number = 10

to_nyc = Distance(200, 'miles')
print('first', to_nyc.number)
to_nyc.number = 100
print('second', to_nyc.number)

print(to_portland.unit)
print(to_portland.number)
print(to_portland.to_meters())
print(to_portland)