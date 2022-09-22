let num = 0
let digits = []
let numbers_for_operation = []
let result = 0

function user_input() {
    let buttons = document.querySelectorAll("button")
    buttons.forEach(button => {
        button.addEventListener("click", (event) => {
            if (button.className == "all-clear") {
                document.getElementById("calculator-screen").value = 0
                digits = []
                numbers_for_operation = []
                result = 0
            } else if (button.className == "number" || button.className == "decimal") {
                digits.push(event.target.value)
                num = convert_to_num(digits)
                document.getElementById("calculator-screen").value = num
            } else if (button.className == "operator") {
                let operation = button.value
                numbers_for_operation.push(num)
                digits = []
                document.getElementById("calculator-screen").value = ""
                if (numbers_for_operation.length == 2) {
                    result = operator(numbers_for_operation[0], numbers_for_operation[1], operation)
                    console.log(result)
                }
            } else {
                numbers_for_operation.push(num)
                document.getElementById("calculator-screen").value = result
            }
        })
    })
}

function convert_to_num(digits_list) {
    return parseFloat(digits_list.join(""))
}

function operator(num1, num2, operation) {
    if (operation == "+") {
        return num1 + num2
    } else if (operation == "-") {
        return num1 - num2
    } else if (operation == "*") {
        return num1 - num2
    } else if (operation == "/") {
        if (num1 == 0) {
            return "Invalid"
        } else {
            return num1 / num2
        }
    }
}

user_input()