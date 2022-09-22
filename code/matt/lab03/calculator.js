const calculator = document.querySelector('.calculator')
const keys = calculator.querySelector('.calculator-keys')
const display = document.querySelector('.calculator-screen')


keys.addEventListener('click', value => {
    if (value.target.matches('button')) {
        const key = value.target
        const action = key.dataset.action
        const keyContent = key.textContent
        const displayedNum = display.textContent
        const previousKeyType = calculator.dataset.previousKeyType
        //If it's a number do below
        if (!action)
            // if the number on the calculator screen is 0 or if it's an operand
            // update it with the text content
            if (displayedNum === "0" || previousKeyType === 'operator') {
                display.textContent = keyContent
                console.log(keyContent)
                // if not, add it to the calculator screen, display the text, and the number that was given
            } else {
                display.textContent = displayedNum + keyContent
            }
        //If the action equals an operand
        if (
            action === 'add' ||
            action === 'subtract' ||
            action === 'multiply' ||
            action === 'divide'
        ) {
            //
            calculator.dataset.previousKeyType = 'operator'
            calculator.dataset.firstValue = displayedNum
            calculator.dataset.operator = action
        }

        if (action === 'decimal') {
            display.textContent = displayedNum + '.'
        }

        if (action === 'clear') {
            console.log('clear key!')
        }
        if (action === 'calculate') {
            const calculate = (n1, operator, n2) => {
                let result = ''

                if (operator === 'add') {
                    result = parseFloat(n1) + parseFloat(n2)
                } else if (operator === 'subtract') {
                    result = parseFloat(n1) - parseFloat(n2)
                } else if (operator === 'multiply') {
                    result = parseFloat(n1) * parseFloat(n2)
                } else if (operator === 'divide') {
                    result = parseFloat(n1) / parseFloat(n2)
                }

                return result
            }

            const firstValue = calculator.dataset.firstValue
            const operator = calculator.dataset.operator
            const secondValue = displayedNum

            display.textContent = calculate(firstValue, operator, secondValue)
        }
    }
})