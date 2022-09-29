
const calcScreen = document.getElementById('calculator-screen')
const choices = document.querySelectorAll('button')


console.log(choices, 'choices')
let nums = []
let lastOperator = ''
let runningSum = 0
let operator = document.querySelectorAll('.operator')
let equal = document.querySelectorAll('.equal-sign')
let allClear = document.querySelectorAll('.all-clear')
let storeSec = []
let data = []

choices.forEach(choice => choice.addEventListener('click', (event) => {// for each method target all method from
    let element = event.target.id
    console.log(element)
    let isNums = parseInt(element)
    // console.log(typeof(isNums))
    console.log(event.target.id)
    console.log(isNums)
    if (isNaN(isNums)) {
        if (element == '='){
            runningSum = eval(runningSum + lastOperator + isNums.join(''))
            console.log(runningSum)
        } 
        
        runningSum = eval(runningSum + element + nums.join('') )
        lastOperator = element
        nums = []
        console.log(runningSum)
        
        
    } if (!isNaN(isNums)) {
        
        // console.log('is number')
        nums.push(event.target.id)
        // console.log(nums)    
    }
    
}))