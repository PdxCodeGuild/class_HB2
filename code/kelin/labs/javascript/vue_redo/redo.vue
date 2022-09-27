<!-- Kelin Ray
Vue Redo Lab
Unit Converter -->

<!-- Unit Converter
Simple version: the user enters the distance and units and the app shows them the converted distance in meters
Complex version: the user also enters output units -->

<!-- Python code
from operator import truediv


feet_to_meters = {'ft': 0.3048}

number_feet = input("\nPlease enter the number of feet: ")

number_feet = int(number_feet)

meters = (feet_to_meters['ft'] * number_feet)

print((number_feet), "feet is", (meters), "meters")

meter = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

while True:
    number = input("Enter the distance: ")
    unit = input("Enter the unit - ft - mi - m - km - yd - in: ")
    if unit == 'ft':
        print((number), "feet is", (int(number) * (meter["ft"])), "meters")
    elif unit == 'mi':
        print((number), "miles is", (int(number) * (meter["mi"])), "meters")
    elif unit == 'm':
        print((number), "meters is", (int(number) * (meter["m"])), "meters")
    elif unit == 'km':
        print((number), "kilometers is", (int(number) * (meter["km"])), "meters")
    elif unit == 'yd':
        print((number), "yards", (int(number) * (meter["yd"])), "meters")
    elif unit == 'in':
        print((number), "inches is", (int(number) * (meter["in"])), "meters")
    else:
        print("Invalid unit")
-->
<script>
  const app = new Vue({
    el: '#app',
    data: {
        message: '',
                startUnit: '',
                endUnit: '',
                distance: '',
                convertedDistance: '',
                units: [{
                    name: 'inches', value: .0254,
                }, {
                    name: 'feet', value: .3048,
                }, {
                    name: 'yards', value: .9144,
                }, {
                    name: 'meters', value: 1,
                }, {
                    name: 'miles', value: 1609.34,
                }, {
                    name: 'kilometers', value: 1000,
                }],
            },
            methods: {
                convert: function () {
                    var unitToMeters = this.distance * this.startUnit.value
                    this.convertedDistance = unitToMeters / this.endUnit.value 
                    this.convertedDistance = Math.round((this.convertedDistance + Number.EPSILON) * 100) / 100
                    this.message = this.distance + ' ' + this.startUnit.name + ' converts to ' + this.convertedDistance + ' ' + this.endUnit.name
                }
            },
            created: function () {

    }
})
</script>

