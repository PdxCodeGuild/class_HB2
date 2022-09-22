// add default values
let calcScreen = document.querySelector(".calculator-string");
let calcKeys = document.querySelectorAll("button");
numbers = []
runningTotal = 0

console.log(calcKeys)

calcKeys.forEach(b => console.log(b))
calcKeys.forEach(b => console.log(b.value))

calcKeys.forEach(b => {
    typeof(b.value) == 'number';
        numbers.push(b.value)
})
console.log(numbers)


// event listener
// iterate between classes
// convert str to nums
// use operators