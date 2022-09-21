navigator.geolocation.getCurrentPosition(position => {
    let lat = position.coords.latitude
    let long = position.coords.longitude

    axios({
        method: 'get',
        url: 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&exclude=hourly,daily&appid=63773348af0d6a9d677e88c0f0170634',
            
      }).then((response) => {
        console.log(response.data["name"])
        let data = response.data
        let locationTitle = document.querySelector("#title")
        title.innerHTML = "<h1>"+ response.data["name"] +"</h1>"
        console.log(locationTitle)


        let unix_timestamp = data["dt"]
        let datetime = new Date(unix_timestamp*1000)
        let dtTitle = document.querySelector("#date")
        dtTitle.innerHTML = "<h3>" + datetime + "</h3>"
        console.log(data)
        console.log(datetime) // Thu Jun 18 2020 05:21:31 GMT-0700 (Pacific Daylight Time)


       
        let weatherMain = document.querySelector("#weather_main")
        weatherMain.innerHTML = "<h3>" + response.data["weather"][0]["main"] + "</h3>"
        console.log(response.data["weather"][0]["main"])
        
        
        
        let weatherIconCode = document.querySelector("#weather_icon")
        weatherIconCode.innerHTML = "<img src='http://openweathermap.org/img/wn/" + response.data["weather"][0]["icon"] + "@2x.png'>"

        console.log(weatherIconCode)

        
    })
    
})



// ppid=${key}&units=imperial