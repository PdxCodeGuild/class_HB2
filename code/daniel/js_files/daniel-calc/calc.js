
let calcScreen = document.querySelector(".calculator-screen");
let buttons = document.querySelectorAll("button");
let keys = document.querySelectorAll(".calculator-keys");
let buttonPressed = []
let runningTotal = 0


buttons.forEach((button) => {
    button.addEventListener('click',(event) => {
        let checkIfNum = parseInt(event.target.value)
        let buttonValue = event.target.value
        if (isNaN(buttonValue) && buttonValue != '.'){

            if (event.target.value == "AC") {
                buttonPressed = 0
                runningTotal = 0
                console.log(event.target.value)
                console.log(buttonPressed)
                console.log(runningTotal)
            }

            if (event.target.value == "=") {
                runningTotal = eval(buttonPressed.join(""))
                buttonPressed = []
                console.log("runningTotal", runningTotal)
                runningTotal = 0
            }
            
            if (event.target.value == "+") {
                if (runningTotal == 0) {
                    buttonPressed.push(buttonValue)
                    console.log("runningTotal", runningTotal)
                    console.log("buttonValue", buttonValue)
                }

            } else if (event.target.value == "-") {
                if (runningTotal == 0) {
                    buttonPressed.push(buttonValue)
                    console.log("runningTotal", runningTotal)
                    console.log("buttonValue", buttonValue)
                } 
                

            } else if (event.target.value == "*") {
                if (runningTotal == 0) {
                    buttonPressed.push(buttonValue)
                    console.log("runningTotal", runningTotal)
                    console.log("buttonValue", buttonValue)

                }

            } else if (event.target.value == "/") {
                if (runningTotal == 0) {
                    buttonPressed.push(buttonValue)
                    console.log("runningTotal", runningTotal)
                    console.log("buttonValue", buttonValue)
                }
            } 
        }

            
        if (!isNaN(checkIfNum) || buttonValue == '.') {
            console.log(buttonPressed)
            buttonPressed.push(buttonValue)
            
        }
    })
})


