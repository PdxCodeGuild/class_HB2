// const nums = ["5", "0", "8", "3", "4", "1", "6"];

userinput = []

function myFunction() {
    let userinput = prompt("Please enter a number", "3");
    if (userinput != null) {
      document.getElementById("myapp").innerHTML =
      "You have entered the following number: " + userinput;
    }
  }

// if userinput is done, then break
