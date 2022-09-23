/* Kelin Ray
Calculator Lab
*/

const screen = document.querySelector(".calculator-screen");
const keys = document.querySelector(".calculator-keys");
const input = null;
const nums = document.querySelector(".equals_to");
const num = document.getElementsByClassName("num");
const period = document.getElementById("period");

// Global Variables
var memory = "0", current = "0", operation = 0; 
const maxChar = 10; 
// Get display
const display = document.querySelector('.calculator-screen');

// Adding a value to screen 
function addValue(dig){ 
     
if ((eval(current) === 0) && (current.indexOf(".") === -1)) { 
        current = dig;
        } else { 
            current += dig;
        } 
 
     display.innerHTML = current; 
}
// Adding a decimal. 
function addDecimal() { 
// If there is no number before decimal add 0.    
  if (current.length === 0) {
      current = "0.";
  } else 
    if (current.indexOf(".") === -1){
      current += ".";
    }
  
  display.innerHTML = current;
}