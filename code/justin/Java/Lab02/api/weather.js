// import {key} from '/secrets.js';

let lat = null
let lon = null

function getLocation(){
    navigator.geolocation.getCurrentPosition(success);

}

function success(position){
    const crd = position.coords;
    lat = crd.latitude;
    lon = crd.longitude;
    console.log(lat + ', ' + lon)
    if(lat != null){
        axios({
            method: 'get',
            url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}&units=imperial`,
        }).then((response) => {
            console.log(response.data);
            console.log(response.data.name);
            console.log(response.data.main['temp']);
            console.log(response.data.weather[0]['description']);

        })
    }
}

window.onload = getLocation()



// axios({
//     method: 'get',
//     url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}`,
// }).then((response) => {
//     console.log(response.data)
// })

