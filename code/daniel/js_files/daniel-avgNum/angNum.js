// let nums = [5, 0, 8, 3, 4, 1, 6]
// let runningSum = 0


// for (n in nums) {
//     runningSum += nums[n]
//     // console.log(n)
// }
// // console.log(runningSum)

// avgNum = runningSum / nums.length
// // console.log(avgNum)


//===================================================

runningSum = 0
userInput = 0
numList = []

let inputBool = true
while (inputBool == true) {
    askNum = prompt("Enter a number or type 'done' when finished: ")
    if (askNum != "done") {
        numList.push(parseInt(askNum))
    }
    else {
        inputBool = false
    }
}
for (n in numList) {
    runningSum += numList[n]
}
avgNum = Number(runningSum) / numList.length   

console.log("running sum:", runningSum, "average num:", avgNum)
console.log(numList)
