function getLocation() {
    navigator.geolocation.getCurrentPosition(position => {
        console.log(position.coords.latitude)
        console.log(position.coords.longitude)
        let lat = position.coords.latitude
        let lon = position.coords.longitude
        console.log(apiKey)
        axios({
            method: 'get',
            url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}appid=${apiKey}`
        }).then((response) => {
            console.log(response.data)
        })
    })
}
console.log(getLocation())


// function showPosition() {
//     document.getElementById("location"), innerHTML = "Latitude: " + position.coords.latitude +
//         "<br>Longitude: " + position.coords.longitude;


// console.log(apiKey)
// axios({
//     method: 'get',
//     url: `https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=${apiKey}`
// }).then((response) => {
//     console.log(response.data);
// }, (error) => {
//     console.log(error);
// })