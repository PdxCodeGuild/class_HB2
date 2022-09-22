/* Kelin Ray
Calculator Lab
*/

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

