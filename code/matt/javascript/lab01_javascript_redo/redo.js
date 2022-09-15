// #Matt Nichols
// #HB2 Lab01Javascript

// #Version 1

//Default list that was given
let nums = [5, 110, 8, 3, 4, 1, 6]
let total = 0

//For loop for running through the list and getting a 'running sum'
for (let num=0; num<nums.length; num++) {
    total += nums[num];
}
//Finding the mean  
let avg = total / nums.length
// alert(avg)

// #Version 2











// function sum(nums) {
//     let total = 0
//     for (let num=0; num<nums.length; num++) {
//         total += nums[num];
//         return total
// }

// #Def function for summing numbers in a list
// def sum(nums):
//     total = 0
//     for num in range(len(nums)):
//         nums_in_list = nums[num]
//         total = total + nums_in_list
//     return total

function userInput() {
    let number = prompt("Enter a number (Make sure there are no spaces)\nType 'done' to exit\n")
    return number
}

function getNums() {
    let array_of_nums = []
    let i=0
    while (i<5) {
        let user_input = userInput()
        array_of_nums.push(user_input)
        i++
        if (user_input == 'done') {
            alert("Thank you for your time")
            break
        }
       let added = 
    }
}






// alert(userInput())


// // #Def function for user input
// def user_input():
//     user = input("Enter a number (Make sure there are no spaces)\nType 'done' to exit\n")
//     return user

// // #Empty list for sum function
// empty_list = []

// // #While loop to take and add the user input to find their running sum
// while True:
// // #For when the user wants to exit the program 
//     response = user_input()
//     if response == 'done':
//         result = "Okay, thank you for your time "
//         print(result)
//         break

// // #To add numbers to the empty list and calculate their sum OR to tell them the input was invalid
//     try:
//         empty_list.append(float(response))
//         added = sum(empty_list)
//         print(added)
//     except:
//         print("Sorry, that wasn't readable. Please make sure you type what is prescribed below. ")
    
// // #If statement catching zero input from user, as well as giving them their total/mean if they do give give valuable input    
// if len(empty_list) == 0:
//     print("Mean = N/A")
// else:
//     print(f'Your total is {added}. {added} divided by {len(empty_list)} is equal to {added / len(empty_list)} ')