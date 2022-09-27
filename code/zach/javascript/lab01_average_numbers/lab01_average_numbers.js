let num_array = []
let sum = 0
let user_input = prompt("Please enter an integer or 'done' to exit")

while(user_input != 'done') {
    num_array.push(user_input)
    user_input = prompt("Please enter another integer or 'done' to exit")
}

for(let i = 0; i < num_array.length; i++) {
    sum += parseInt(num_array[i])
}

let arr_avg = sum / num_array.length

alert("The average of " + num_array + " is " + arr_avg)