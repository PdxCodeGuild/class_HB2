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
    lat = position.coords.latitude
    long = position.coords.longitude
    fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&appid=${key}`)
    
    // &exclude=hourly,daily
    // &units=imperial

    .then(function (response) {
        console.log(response.data);

    // .then(response => response.json())
    // console.log(response.json)
    });
})
}
