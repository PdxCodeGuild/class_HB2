
// function myFunction() {
//     let userinput = prompt("Please enter a number", "3");
//     if (userinput != null) {
//       document.getElementById("myapp").innerHTML =
//       "You have entered the following number: " + userinput;
//     }
//   }


numValues = []

function addList() {
  let numInput = document.querySelector('#num_input')
  let numValue = parseFloat(numInput.value)
  numValues.push(numValue)
  document.getElementById("myapp").innerHTML = "You have entered the following number(s): " + numValues;
  // console.log(num_value)
}

function calculateAverage(array) {
  let total = 0;
  let count = 0;

  array.forEach(function(item) {
      total += item;
      count++;
  });

  return total / count;
}

function calculateList() {
  let avg = calculateAverage(numValues)
  // console.log(avg)
  document.getElementById("mycalc").innerHTML = "The average of your inputed numbers is: " + avg;
}

// if (numInput != null) {
//   document.getElementById("myapp").innerHTML =
//   "You have entered the following number: " + numInput;
//   }