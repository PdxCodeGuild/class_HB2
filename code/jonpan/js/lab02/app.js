function showPosition(position) {
    document.getElementById("location").innerHTML = "Latitude: " + position.coords.latitude +
    "<br>Longitude: " + position.coords.longitude;
  }

function getLocation() {
    navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
    showPosition(position)
})
}

function getWeather() {
    navigator.geolocation.getCurrentPosition(position => {
        let lat = position.coords.latitude
        let long = position.coords.longitude

        axios({
            method: 'get',
            url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${long}&appid=${key}&units=imperial`
          })
            .then((response) => {
              console.log(response.data)
              // document.getElementById("location2").innerHTML = response.data.name
              let unix_timestamp = 1592482891
              let datetime = new Date(unix_timestamp*1000)
              document.getElementById("datetime").innerHTML = "Current Time: " + datetime
              document.getElementById("weather").innerHTML = "Current Weather: " + response.data.weather['0']['main'] 
              document.getElementById("temp").innerHTML = "Current Temperature: " + response.data.main['temp'] + " degrees Fahrenheit in " + response.data.name 
              let img = document.createElement('img')
              img.src = 'http://openweathermap.org/img/wn/' + response.data.weather['0']['icon'] + '.png'
              document.getElementById("weather").appendChild(img)
            })
          })
}
