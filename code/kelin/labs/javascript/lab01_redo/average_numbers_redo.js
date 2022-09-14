/* Kelin Ray

Lab 1: JavaScript Redo: Average Numbers
Version 1
Pick a Python lab and re-do it in JavaScript. You should first try to write them using JavaScript's prompt and alert in place of Python's input and print. */

/* Python code

nums = [5, 0, 8, 3, 4, 1, 6]
x = sum(nums)
i = len(nums)
answer = (x / i)
print(answer) */

var nums = [5, 0, 8, 3, 4, 1, 6];

// Get sum of numbers

var sum = 0;
for (var i in nums) {
    sum += nums[i];
}
// console.log(sum) 27
// Get number in array

var numslen = nums.length;

// console.log(numslen) 7
// Get average

var average = sum / numslen;

// console.log(average) 3.857142857142857
// Print average in alert

// alert(average)


/* Version 2 Python

user_nums = []

while True:
    user = input("Enter numbers to average, and type 'done' to calculate: ")
    if user == "done":
        print((sum(user_nums)) / (len(user_nums)))
    else:
        user_nums.append(int(user))
        print(user_nums) */


function num_prompt() {
    var i = 0;
    var sum = 0;

    // Variable to keep sum of numbers

    do {
        var number = prompt("Enter a number to average");
        sum += parseInt(number); 
        i++;

        // Get sum of numbers
          
        document.write("Number: " + number);
        document.write("<br>"); 
        
        // Displays numbers on page
          
    }
    while (i < 5); 

    // Prompts for a number 5 times
          
    document.write('Your average : ' + sum / i);
    }
    num_prompt();

    // Displays avererage of numbers on page