// Pass GetCurrentPosition a function that defines latitude and longitude
navigator.geolocation.getCurrentPosition(position => {
    let lat = position.coords.latitude
    let lon = position.coords.longitude

    // Use axios to execute the API call then pass the response into the html page
    axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + key + '&units=imperial'
    }).then((response) => {
        console.log(response.data)

        // Get location to display on html page
        document.getElementById('location').innerHTML = response.data.name

        // Convert unix timestamp to long date/time and display on html page
        let unix_timestamp = response.data.dt
        let datetime = new Date(unix_timestamp * 1000)
        document.getElementById('datetime').innerHTML = datetime

        // Display weather on html page
        document.getElementById('weather_description').innerHTML = "It is currently " + response.data.weather['0']['main'] + " and " + response.data.main['temp'] + " degrees Fahrenheit"

        // Create an img element and append to the DOM
        let img = document.createElement('img')
        img.src = 'http://openweathermap.org/img/wn/' + response.data.weather['0']['icon'] + '.png'
        document.getElementById('weather').appendChild(img)
    })
})