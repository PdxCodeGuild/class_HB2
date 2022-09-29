// const calculator = document.querySelector('.calculator')
// const keys = calculator.querySelector('.calculator-keys')
// const display = document.querySelector('.calculator-screen')


// keys.addEventListener('click', value => {
//     if (value.target.matches('button')) {
//         const key = value.target
//         const action = key.dataset.action
//         const keyContent = key.textContent
//         const displayedNum = display.textContent
//         const previousKeyType = calculator.dataset.previousKeyType
//         const storedValue = []
//         //If it's a number do below
//         if (!action)
//             // if the number on the calculator screen is 0 or if it's an operand
//             // update it with the text content
//             if (displayedNum === "0") {
//                 display.textContent = keyContent
//                 // console.log(keyContent)
//                 console.log(display.textContent)
//                 // if not, add it to the calculator screen, display the text, and the number that was given
//             }
//             else if (previousKeyType === 'operator') {
//                 display.textContent = displayedNum
//             }
//             else {
//                 display.textContent = displayedNum + keyContent
//                 console.log(display.textContent)
//             }
//         //If the action equals an operand
//         if (
//             action === 'add' ||
//             action === 'subtract' ||
//             action === 'multiply' ||
//             action === 'divide'
//         ) {
//             //
//             calculator.dataset.previousKeyType = 'operator'
//             calculator.dataset.firstValue = displayedNum
//             calculator.dataset.operator = action
//         }

//         if (action === 'decimal') {
//             display.textContent = displayedNum + '.'
//         }

//         if (action === 'clear') {
//             console.log('clear key!')
//         }
//         if (action === 'calculate') {
//             const calculate = (n1, operator, n2) => {
//                 let result = ''

//                 if (operator === 'add') {
//                     result = parseFloat(n1) + parseFloat(n2)
//                 } else if (operator === 'subtract') {
//                     result = parseFloat(n1) - parseFloat(n2)
//                 } else if (operator === 'multiply') {
//                     result = parseFloat(n1) * parseFloat(n2)
//                 } else if (operator === 'divide') {
//                     result = parseFloat(n1) / parseFloat(n2)
//                 }

//                 return result
//             }

//             const firstValue = calculator.dataset.firstValue
//             console.log(firstValue)
//             const operator = calculator.dataset.operator
//             console.log(operator)
//             const secondValue = displayedNum
//             console.log(secondValue)

//             display.textContent = calculate(firstValue, operator, secondValue)
//         }
//     }
// })

function convertToNum(convertToNum) {
    return parseFloat(convertToNum.join(""))
}

function calculator() {
    // To grab all the button elements with the queryselectorall. keyword all
    let keyInput = document.querySelectorAll("button")

    // 
    let arrayOfStrings = []
    let arrayOfNums = []
    let num = 0
    let result = 0
    let last_operator = ""

    // for '''keyinput''' add an event listener to it. That way everytime you click a key on the calculator it'll do something
    keyInput.forEach(button => {
        button.addEventListener("click", (event) => {

            // If user selects AC button, clear all variable values
            if (button.className == "all-clear") {
                document.getElementById("calculator-screen").value = 0
                restart = num = 0, arrayOfStrings = [], arrayOfNums = [], result = 0, last_operator = ""
                return restart

                // If key pressed is equal to a number than do what is below
            } else if (button.className == "number") {

                //When key is pressed and the event is activated target the value of said key
                //They'll still be in string format, hence the name '''arrayOfStrings'''
                arrayOfStrings.push(event.target.value)

                // '''nums''' will now convert our array of strings to numbers using the function above this function 
                num = convertToNum(arrayOfStrings)

                //numbers presented on calc screen
                document.getElementById("calculator-screen").value = num


            }
            // If key pressed is equal to a number than do what is below
            else if (button.className == "decimal") {

                //When key is pressed and the event is activated target the value of said key
                //They'll still be in string format, hence the name '''arrayOfStrings'''
                arrayOfStrings.push(event.target.value)

                num = convertToNum(arrayOfStrings)

                //decimal presented on calc screen
                document.getElementById("calculator-screen").value = num
            }
            // For when a user keys an operand
            else if (button.className == "operator") {
                arrayOfStrings = []
                document.getElementById("calculator-screen").value = ""

                // When an operand is selected, add the strings that we converted to integers to the list 
                if (document.getElementById("calculator-screen").value = "" == last_operator) {
                    arrayOfNums.push(num)
                    result = num

                    // When an operator is selected and last_operator has a value run operator on list; update result
                } else {
                    arrayOfNums.push(num)
                    result = operator(arrayOfNums[0], last_operator, arrayOfNums[1],)
                    arrayOfNums = [result]
                }

                // Display current_num
                document.getElementById("calculator-screen").value = result
                last_operator = button.value

                // If user clicks the equal sign
            } else if (button.className == "equal-sign") {
                if (last_operator == "") {
                    result = num
                } else {
                    arrayOfNums.push(num)
                    result = calculate(arrayOfNums[0], last_operator, arrayOfNums[1],)
                }
                document.getElementById("calculator-screen").value = result
                num = 0
                arrayOfStrings = []
                arrayOfNums = []
                result = 0
                last_operator = ""
            }
        })
    })
}



function calculate(n1, operator, n2,) {
    if (operator == "+") {
        return n1 + n2
    } else if (operator == "-") {
        return n1 - n2
    } else if (operator == "*") {
        return n1 * n2
    } else if (operator == "/") {
        return n1 / n2
    }
}

calculator()
//                 if (operator === 'add') {
//                     result = parseFloat(n1) + parseFloat(n2)
//                 } else if (operator === 'subtract') {
//                     result = parseFloat(n1) - parseFloat(n2)
//                 } else if (operator === 'multiply') {
//                     result = parseFloat(n1) * parseFloat(n2)
//                 } else if (operator === 'divide') {
//                     result = parseFloat(n1) / parseFloat(n2)
//                 }

//                 return result