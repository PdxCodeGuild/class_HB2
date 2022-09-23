/* Kelin Ray
Calculator Lab
*/

// Cleared calculator
const calculator = {
  displayValue: "0",
  firstOperand: null,
  waitingForSecondOperand: false,
  operatior: null,
};
// Display screen
function updateDisplay() {
  const display = document.querySelector(".calculator-screen")
  display.value = calculator.displayValue;
};

updateDisplay();
// Updates screen with keys clicked
const keys = document.querySelector(".calculator-keys");
keys.addEventListener("click", (event) => {
  const {
      target
  } = event;
// Gets numbers from buttons
  if (!target.matches("button")) { 
      return;
  }
// Gets operators
  if (target.classList.contains("operator")) {
      handleOperator(target.value);
      updateDisplay();
      return;
  }
// Adds decimal
  if (target.classList.contains("decimal")) {
      inputDecimal(target.value);
      updateDisplay();
      return;
  }
// Resets calculator and clears display
  if (target.classList.contains("all-clear")) {
      resetCalculator();
      updateDisplay();
      return;
  }
  inputDigit(target.value);
  updateDisplay();
});
// Gets second number input
function inputDigit(digit) {
  const {
      displayValue,
      waitingForSecondOperand
  } = calculator;
// Displays second number
  if (waitingForSecondOperand === true) {
      calculator.displayValue = digit;
      calculator.waitingForSecondOperand = false;
  } else {
      calculator.displayValue = displayValue === '0' ? digit : displayValue + digit;
  }
// Sets the second number to 0 if no input

};
// Decimal function
function inputDecimal(dot) {
  if (calculator.waitingForSecondOperand === true) return;

  // If the `displayValue` does not contain a decimal point
  if (!calculator.displayValue.includes(dot)) {
      // Append the decimal point
      calculator.displayValue += dot;
  }
};
// Adds number after decimal
function handleOperator(nextOperator) {
  const {
      firstOperand,
      displayValue,
      operator
  } = calculator
  const inputValue = parseFloat(displayValue);
// Gets second number to calculate
  if (operator && calculator.waitingForSecondOperand) {
      calculator.operator = nextOperator;

      return;
  }
// Inputs decimal number
  if (firstOperand == null) {
      calculator.firstOperand = inputValue;
  } else if (operator) {
      const currentValue = firstOperand || 0;
      const result = performCalculation[operator](currentValue, inputValue);
// Displays 0 before decimal number
      calculator.displayValue = String(result);
      calculator.firstOperand = result;
  }
// Gets additonal operand number
  calculator.waitingForSecondOperand = true;
  calculator.operator = nextOperator;
};
// Operator calculations
const performCalculation = {
  '/': (firstOperand, secondOperand) => firstOperand / secondOperand,

  '*': (firstOperand, secondOperand) => firstOperand * secondOperand,

  '+': (firstOperand, secondOperand) => firstOperand + secondOperand,

  '-': (firstOperand, secondOperand) => firstOperand - secondOperand,

  '=': (firstOperand, secondOperand) => secondOperand
};
// Clears display and resets calculator
function resetCalculator() {
  calculator.displayValue = '0';
  calculator.firstOperand = null;
  calculator.waitingForSecondOperand = false;
  calculator.operator = null;
};

/* To Do

Display equation on screen with operators and decimal numbers

*/