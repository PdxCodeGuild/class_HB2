
// let nums = [5, 0, 8, 3, 4, 1, 6]

const nums = ["5", "0", "8", "3", "4", "1", "6"];

let text = "<ul>";
nums.forEach(myFunction);
text += "</ul>";

function myFunction(value) {
  text += "<li>" + value + "</li>";
}


