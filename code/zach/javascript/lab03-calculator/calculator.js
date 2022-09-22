let num = 0
let digits = []
let result = 0

function user_input() {
    let buttons = document.querySelectorAll("button")
    buttons.forEach(button => {
        button.addEventListener("click", (event) => {
            if (button.className == "all-clear") {
                document.getElementById("calculator-screen").value = 0
                digits = []
                result = 0
            } else if (button.className == "number" || button.className == "decimal") {
                digits.push(event.target.value)
                num = convert_to_num(digits)
                document.getElementById("calculator-screen").value = num
            } else if (button.className == "operator") {
                let operation = button.value
                digits = []
                document.getElementById("calculator-screen").value = ""
                result = operator(result, num, operation)
                console.log(result)
            } else if (button.className == "equal-sign") {
                digits = []
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