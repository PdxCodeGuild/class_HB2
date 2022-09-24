// add default values
let calcScreen = document.querySelector(".calculator-screen");
let buttons = document.querySelectorAll("button");
numbers = []
runningTotal = 0

console.log(buttons[0])

for (let button of buttons){
button.addEventListener('click', function(){
    alert(button.value)
})}


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