const eight = document.getElementById('eight')
const calcScreen = document.getElementById('calculator-screen')
const choices = document.querySelectorAll('button')
console.log(eight)
console.log(choices)
let string = ""
let results 
let nums = []
let operator = document.querySelectorAll('operator')
let equal = document.querySelectorAll('equal-sign')
let allClear = document.querySelectorAll('all-clear')
let calcTest = document.getElementById('calc-test')

let calcBtn 
choices.forEach(choice=>choice.addEventListener('click', (event)=>{// for each method target all method from
//    console.log(event,'events')
    calcBtn=event.target.id // targeting id from input 
    // console.log(calcBtn, 'user choice')
    calcScreen.value= calcBtn
   calcScreen.value = results += calcBtn
   nums.push(calcBtn)
   console.log(nums, 'nums')
   for(i =0; i<nums.length;i++){
    //    console.log(nums[i],i,'testing nums')
    if (nums[i]==='+' || "-"||'/'||'*'){
        console.log('yay')
    }

   }
    
}))
// if (calcBtn in operator){
    //     nums.push(calcBtn)
    // }
    // if (calcBtn=='+'){
        //   results=results + parseInt(nums.join())
        // } 
        // console.log(results )
        // console.log(nums)
        // console.log(calcBtn)
        // console.log(string)
        // string = string + calcBtn;
// document.querySelector('input').value= string


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