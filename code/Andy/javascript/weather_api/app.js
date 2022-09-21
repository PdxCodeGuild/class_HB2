navigator.geolocation.getCurrentPosition(position => {
  let lat = position.coords.latitude
  let lon = position.coords.longitude
  
  
  
  // let theUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${key}`
  axios({
    method: 'get',
    url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${key}&units=imperial`
  }).then((response) => { // then a promise to get it back after waiting
    console.log(response, 'response')
    // console.log(response.data) //
    let unix_timestamp = (response.data.dt) // it has to be .dt and not the numbers because then it would just be for my timezone 
    let datetime = new Date(unix_timestamp*1000)
    // console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)
    // console.log(response.data.weather[0]['icon'])
    let icon = response.data.weather[0]['icon']
    let img = document.getElementById('icon')
    img.src = `http://openweathermap.org/img/wn/${icon}.png`
    document.getElementById('temp').innerHTML = response.data.main["temp"] +" F"
    // temp.innerHTML = response.data.main["temp"]
    // console.log(response.data.name)
    document.getElementById('city').innerHTML = response.data.name
    document.getElementById('feels').innerHTML = response.data.main['feels_like']

  })  //  add CDN to be able to use this <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
})
