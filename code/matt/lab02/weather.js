function getLocation() {
    navigator.geolocation.getCurrentPosition(position => {
        let lat = position.coords.latitude
        let lon = position.coords.longitude

        axios({
            method: 'get',
            url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=imperial`
        }).then((response) => {
            let unix_timestamp = (response.data['dt'])
            let datetime = new Date(unix_timestamp * 1000)
            let icon = response.data['weather']['0']['icon']
            let img = document.getElementById('icon')
            img.src = `http://openweathermap.org/img/wn/${icon}.png`
            let location = document.getElementById('location')
            location.innerText = response.data['name']
            let temp = document.getElementById('temp')
            temp.innerText = "Current Temp: " + response.data['main']['temp'] + '°F |' + " Feels Like: " + response.data['main']['feels_like'] + '°F'
            let minMax = document.getElementById('min_max')
            minMax.innerText = "Min Temp: " + response.data['main']['temp_min'] + '°F |' + " Max Temp: " + response.data['main']['temp_max'] + '°F'
            let conditions = document.getElementById('conditions')
            conditions.innerText = response.data['weather']['0']['description'] + ' |' + " Wind: " + response.data['wind']['speed'] + 'MPH'
            console.log(datetime);
            console.log(response.data)

        }, (error) => {
            console.log(error);
        })
    })
}
console.log(getLocation())