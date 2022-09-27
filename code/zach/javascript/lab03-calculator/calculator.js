let num = 0
let digits = []
let num_list = []
let result = 0
let last_operator = ""

function user_input() {
    // Select all button elements
    let buttons = document.querySelectorAll("button")
    // For each button add an on click event
    buttons.forEach(button => {
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

user_input()