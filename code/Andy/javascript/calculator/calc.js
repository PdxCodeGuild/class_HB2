const eight = document.getElementById('eight')
const choices = document.querySelectorAll('button')
console.log(eight)
console.log(choices)
let string = ""
let results = 0
let nums = []
let operator = document.querySelectorAll('operator')

let calcBtn 
choices.forEach(choice=>choice.addEventListener('click', (event)=>{
    calcBtn=event.target.id
    if (calcBtn in operator){
        nums.push(calcBtn)
    }
    if (calcBtn=='+'){
        results=results + parseInt(nums.join())
    } 
    console.log(results )
    console.log(nums)
    // console.log(calcBtn)
    // string = string + calcBtn;
    // console.log(string)
    // document.querySelector('input').value= string

}))
// function(choice){
//     choice.addEventListener()
//     choice *2
// }

// let seven_btn = document.querySelector('#seven');
// // document.addEventListener('click', function() {
// //     alert('hello world!');
// // }); 
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });     
// let eight_btn = document.querySelector('#eight');
// eight_btn.addEventListener('click', function() {
//     alert('hello world!');
// });    
// let nine_btn = document.querySelector('#nine');
// nine_btn.addEventListener('click', function() {
//     alert('hello world!');
// });    
//  let four_btn = document.querySelector('#four');
// four_btn.addEventListener('click', function() {
//     alert('hello world!');
// });    
// let five_btn = document.querySelector('#five');
// five_btn.addEventListener('click', function() {
//     alert('hello world!');
// });    
// let six_btn = document.querySelector('#six');
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });   
// let one_btn = document.querySelector('#one');
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });   
// let two_btn = document.querySelector('#two');
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });    
// let three_btn = document.querySelector('#three');
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });     let seven_btn = document.querySelector('#seven');
// console.log(seven_btn)
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });     let seven_btn = document.querySelector('#seven');
// console.log(seven_btn)
// seven_btn.addEventListener('click', function() {
//     alert('hello world!');
// });     