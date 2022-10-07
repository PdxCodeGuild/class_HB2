var display = ""
var first = 0
var second = 0
var calculating = 0
var type = ""
var wipe = 0
var dec = 0

function updateScreen(input) {
  document.getElementById('calculator-screen').value = input
}

function number(input) {
  if (wipe == 1) {
    display = input
    wipe = 0
  } else if (calculating == 0) {
    display = display += input
  } else {
    display = input
    calculating = 0
  }

  updateScreen(display)
}

function allclear() {
  display = ""
  updateScreen("")
}

function decimal() {
  if (dec == 0) {
    if (display == "") {
      display = "0."
      updateScreen(display)
    } else {
      display = display += "."
      updateScreen(display)
    }
    dec = 1
  }
}

function solve() {
  let answer = 0
  second = display

  if (type == "add") {
    answer = parseFloat(first) + parseFloat(second)
    display = answer.toString()
    updateScreen(display)
  } else if (type == "sub") {
    answer = parseFloat(first) - parseFloat(second)
    display = answer.toString()
    updateScreen(display)
  } else if (type == "mult") {
    answer = parseFloat(first) * parseFloat(second)
    display = answer.toString()
    updateScreen(display)
  } else if (type == "div") {
    answer = parseFloat(first) / parseFloat(second)
    display = answer.toString()
    updateScreen(display)
  }

  first = "0"
  second = "0"
  calculating = 0
  wipe = 1
  type = ""
  dec = 0
}

function domath(operation) {
  calculating = 1
  first = display
  type = operation
  dec = 0
}
