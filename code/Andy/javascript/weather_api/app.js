let lat = 3.14
let lon = 4.13

// let theUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${key}`
axios({
    method: 'get',
    url: `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&exclude=hourly,daily&appid=${key}&units=imperial`
  }).then((response) => {
    console.log(response.data)

  })  //  add CDN to be able to use this <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>