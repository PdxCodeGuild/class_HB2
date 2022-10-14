<!-- Kelin Ray
Vue Redo Lab
Unit Converter -->

<!-- Unit Converter
Simple version: the user enters the distance and units and the app shows them the converted distance in meters
Complex version: the user also enters output units -->

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

