// add default values
let calcScreen = document.querySelector(".calculator-screen");
let buttons = document.querySelectorAll("button");
let keys = document.querySelectorAll(".calculator-keys");
let operatorPressed = ""
let numberPressed = []
let runningTotal = 0

// console.log(buttons[0])

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
            runningTotal = eval(runningTotal + buttonValue + numberPressed.join(""))
            numberPressed = []
            operatorPressed = buttonValue
            }
// ===========
            // let currentValue = numberPressed.join("")
//             if (event.target.value == "+") {
//                 runningTotal = parseInt(runningTotal) + parseInt(currentValue)
//                 numberPressed = []
//                 operatorPressed = event.target.value
//                 console.log(runningTotal)
//             } else if (event.target.value == "-") {
//                 runningTotal = parseInt(runningTotal) - parseInt(currentValue)
//                 numberPressed = []
//                 console.log(runningTotal)
//             } else if (event.target.value == "*") {
//                 runningTotal = parseInt(runningTotal) * parseInt(currentValue)
//                 numberPressed = []
//                 console.log(runningTotal) 
//             } else if (event.target.value == "/") {
//                 runningTotal = parseInt(runningTotal) / parseInt(currentValue)
//                 numberPressed = []
//                 console.log(runningTotal)
//             } else if (event.target.value == "=") {
//                 runningTotal = eval(runningTotal + operatorPressed + numberPressed.join("")) 
//                 console.log(runningTotal)
//             }

// ============
            // console.log(buttonValue)
        if (!isNaN(checkIfNum) || buttonValue == '.') {
            console.log(numberPressed)
            numberPressed.push(buttonValue)
            // console.log(buttonValue)
        }
        

        // console.log(operatorPressed)
        // console.log(numberPressed)
    })

})


