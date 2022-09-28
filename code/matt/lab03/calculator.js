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


let num = 0
let digits = []
let num_list = []
let result = 0
let last_operator = ""

function calculator() {
    // Select all button elements
    let keyInput = document.querySelectorAll("button")
    // For each button add an on click event
    keyInput.forEach(button => {
        button.addEventListener("click", (event) => {

            // If user selects AC button, clear all variable values
            if (button.className == "all-clear") {
                document.getElementById("calculator-screen").value = 0
                num = 0
                digits = []
                num_list = []
                result = 0
                last_operator = ""

                // If user clicks a number or decimal button push each digit to a list and then convert to a float to be displayed on screen
            } else if (button.className == "number" || button.className == "decimal") {
                digits.push(event.target.value)
                num = convert_to_num(digits)
                document.getElementById("calculator-screen").value = num

                // If user clicks an operator
            } else if (button.className == "operator") {
                digits = []
                document.getElementById("calculator-screen").value = ""

                // When an operator is selected, add number to list 
                if (last_operator == "") {
                    num_list.push(num)
                    result = num

                    // When an operator is selected and last_operator has a value run operator on list; update result
                } else {
                    num_list.push(num)
                    result = operator(num_list[0], num_list[1], last_operator)
                    num_list = [result]
                }

                // Display current_num
                document.getElementById("calculator-screen").value = result
                last_operator = button.value

                // If user clicks the equal sign
            } else if (button.className == "equal-sign") {
                if (last_operator == "") {
                    result = num
                } else {
                    num_list.push(num)
                    result = operator(num_list[0], num_list[1], last_operator)
                }
                document.getElementById("calculator-screen").value = result
                num = 0
                digits = []
                num_list = []
                result = 0
                last_operator = ""
            }
        })
    })
}

function convert_to_num(digits_list) {
    return parseFloat(digits_list.join(""))
}

function operator(num1, num2, operation) {
    console.log(num1 + " " + num2 + " " + operation)
    if (operation == "+") {
        return num1 + num2
    } else if (operation == "-") {
        return num1 - num2
    } else if (operation == "*") {
        if (num1 == 0) {
            return num2
        }
        return num1 * num2
    } else if (operation == "/") {
        if (num1 == 0) {
            return "Invalid"
        } else {
            return num1 / num2
        }
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