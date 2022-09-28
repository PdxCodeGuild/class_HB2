
let calcScreen = document.querySelector(".calculator-screen");
let buttons = document.querySelectorAll("button");
let keys = document.querySelectorAll(".calculator-keys");
let operatorPressed = ""
let numberPressed = []
let operator = []
let runningTotal = 0
let currentValue = numberPressed.join("")


buttons.forEach((button) => {
    button.addEventListener('click',(event) => {
        let checkIfNum = parseInt(event.target.value)
        let buttonValue = event.target.value
        if (isNaN(buttonValue) && buttonValue != '.'){
            if (event.target.value == "=") {
                runningTotal = eval(runningTotal + operatorPressed + numberPressed.join(""))
                numberPressed = []
                console.log(runningTotal)
                runningTotal = 0
            }
            
            if (event.target.value == "+") {
                console.log(runningTotal)
                runningTotal = eval(runningTotal + buttonValue + numberPressed.join(""))
                numberPressed = []
                operatorPressed = buttonValue
                console.log(runningTotal)


            } else if (event.target.value == "-") {
                if (runningTotal == 0) {
                    console.log(runningTotal)
                    numberPressed.push(buttonValue)
                    runningTotal = eval(numberPressed + buttonValue + numberPressed.join(""))
                } else {
                    !!!!!!!!!!!!!!!!!!!!!! needs work !!!!!!!!!!!!!!!!!!!!!!!!
                }

                    numberPressed.push(buttonValue)
                    operator.push(event.target.value)
                runningTotal = eval(runningTotal + operator + numberPressed.join(""))
                numberPressed = []
                operator = []
                
                console.log(runningTotal)
            } else if (event.target.value == "*") {
                runningTotal = eval(runningTotal + buttonValue + numberPressed.join(""))
                numberPressed = []
                operatorPressed = buttonValue
                console.log(runningTotal) 
            } else if (event.target.value == "/") {
                runningTotal = eval(runningTotal + buttonValue + numberPressed.join(""))
                numberPressed = []
                operatorPressed = buttonValue
                console.log(runningTotal)
            } 
            
        }

            
        if (!isNaN(checkIfNum) || buttonValue == '.') {
            console.log(numberPressed)
            numberPressed.push(buttonValue)
            
        }
    })
})


