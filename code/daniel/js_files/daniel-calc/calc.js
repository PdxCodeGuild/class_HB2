// add default values
let calcScreen = document.querySelector(".calculator-screen");
let buttons = document.querySelectorAll("button");
let keys = document.querySelectorAll(".calculator-keys");
operatorPressed = []
numberPressed = []
runningTotal = 0

// console.log(buttons[0])

buttons.forEach((button) => {
    button.addEventListener('click',(event) => {
        let checkIfNum = parseInt(event.target.value)
        let buttonValue = event.target.value
        if (isNaN(checkIfNum)) {
            let currentValue = numberPressed.join("")
            // console.log(parseInt(currentValue) + parseInt(currentValue))
            if (event.target.value == "+") {
                runningTotal = parseInt(runningTotal) + parseInt(currentValue)
                console.log(runningTotal)
                // console.log(buttonValue)
            }
            // console.log(buttonValue)
        } else {
            numberPressed.push(buttonValue)
            // console.log(buttonValue)

            ##make !NaN
        }
        

        // console.log(operatorPressed)
        // console.log(numberPressed)
    })

})



// buttons.forEach(b => {
//     typeof(b.value) == 'NaN';
//         numbers.push(b.value)
//         console.log(numbers)
// })



// console.log(button)

// buttons.forEach(b => console.log(b))
// buttons.forEach(b => console.log(b.value))


// for (const key of Object.keys(buttons)) {
//     console.log(`${key} => ${buttons[key]}`)

// }









// buttons.forEach(b => {
//     typeof(b.value) == 'number';
//         numbers.push(b.value)
// Object.keys(numbers).forEach(b => {
//     console.log(b, ':', numbers[b].temp)
// })


// })
    




// event listener
// iterate between classes
// convert str to nums
// use operators