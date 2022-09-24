// add default values
let calcScreen = document.querySelector(".calculator-screen");
let buttons = document.querySelectorAll("button");
numbers = []
runningTotal = 0

console.log(buttons[0])

buttons.forEach((button) => {
    button.addEventListener('click',(event) => {
        console.log(event.target.value)
    })
})


if (target.matches("button")) {
    return;
}

buttons.forEach(b => {
    typeof(b.value) == 'NaN';
        numbers.push(b.value)
        console.log(numbers)
})



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