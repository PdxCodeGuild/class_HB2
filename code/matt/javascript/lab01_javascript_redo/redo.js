// #Matt Nichols
// #HB2 Lab01Javascript

// #Version 1

//Default list that was given
let nums = [5, 110, 8, 3, 4, 1, 6]
let total = 0

//For loop for running through the list and getting a 'running sum'
for (let num = 0; num < nums.length; num++) {
    total += nums[num];
}
//Finding the mean  
let avg = total / nums.length
// alert(avg)

// #Version 2

//Function for future user input
function userInput() {
    let number = prompt("Enter a number (Make sure there are no spaces)\nType 'done' to exit\n")
    return number
}

//Function for gathering the user input from the function above and calculating it
function getNums() {
    //To store the users numbers
    let array_of_nums = []
    let i = 0

    while (i < 100) {
        let user_input = userInput()
        i++

        // To break out of it when wanted
        if (user_input == 'done') {
            alert("Thank you for your time")
            break
        }


        // to add the numbers to the list and convert them into integers instead of strings
        array_of_nums.push(parseInt(user_input))
        let sum = 0
        for (const value of array_of_nums) {
            sum += value;
        }

        let mean = sum / i

        alert('Your current numbers are: ' + array_of_nums + ' | Your average is: ' + mean)
    }
}