function user_input() {
    let nums = []
    let buttons = document.querySelectorAll("button")
    buttons.forEach(button => {
        button.addEventListener("click", (event) => {
            // If button.className == "number" || "decimal" else if == "operator" then call the appropriate function else clear etc.
            nums.push(event.target.value)
            console.log(nums)
        })
    })
}

function add_nums(num1=0, num2) {
    return num1 + num2
}

function subtract_nums(num1=0, num2) {
    return num1 - num2
}

function divide_nums(num1, num2) {
    return num1 / num2
}

function calculator() {
    user_input()
}

calculator()