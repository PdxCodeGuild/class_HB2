var x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}

function getWeather() {
    navigator.geolocation.getCurrentPosition(position => {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)
        let lat = position.coords.latitude
        let lon = position.coords.longitude
        axios({
            method: 'get',
            url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}`
          })
          
          .then((response) => {
            console.log(response.data)
          })
        })

}

function getWeather()
  