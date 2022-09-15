// Arithematic and numbers
// let x = 1
// let y = 1.5
// let a = 5 + 1 // 6
// let b = 5 - 1 // 4
// let c = 2 * 3 // 6
// let d = 3 / 2 // 1.5
// let e = 2 % 3 // 2

// a += 4

// Math.abs(-4)    // 4 - absolute value
// Math.sqrt(16)   // 4.0 - square root
// Math.min(5, 6)  // 5 - the smaller of the two
// Math.max(5, 6)  // 6 - the larger of the two
// Math.floor(4.5) // 4 - always round down
// Math.ceil(4.5)  // 5 - always rounds up
// Math.round(4.5) // 5 - round to the nearest integer
// Math.random()   // get a random number between 0 and 1, but not including 1
// Math.pow(5, 2)  // 25 - exponentiation
// Math.PI         // 3.1415... pi
// Math.sin(0)     // 0.0 - sine operator
// Math.cos(0)     // 1.0 - cosine operator

// console.log(Math.random()) // random number between 0 and 1
// console.log(Math.random()*20) // random number between 0 and 20
// console.log(20 + Math.random()*20) // random number between 20 and 40
// console.log(Math.floor(20 + Math.random()*20)) // random *integer* between 20 and 40
// let letters = ['a', 'b', 'c']
// console.log(letters[Math.floor(Math.random()*letters.length)]) // random element

// function randint(a, b) {
//     return Math.floor(a + Math.random()*(b-a+1))
// }

// function randomChoice(arr) {
//     let i = randint(0, arr.length-1)
//     return arr[i]
// }

// let x = randint(1, 10) // a random number between 1 and 10
// console.log(x)

// let fruits = ['apples', 'bananas', 'pears']
// console.log(randomChoice(fruits)) // get a random element out of an array

// Conditionals
// let x = 90
// if(x < 66) {
//     alert('cold')
// } else if( x < 80 ) {
//     alert('warm')
// } else {
//     alert('hot')
// }

// Strings
let a = 'hello world!'
let b = "hello world!"

function getFullName(title, fname, lname, degree) {
    return `${title} ${fname} ${lname}, ${degree}`
}
// returns 'Rear Admiral Grace Hopper, PhD'
getFullName('Rear Admiral', 'Grace', 'Hopper', 'PhD')

function showYourWork(num1, num2) {
    return `${num1} + ${num2} = ${num1 + num2}`
}
// returns '3 + 4 = 7'
// showYourWork(3, 4)

// let s = 'this is a really long\
// string, so long that we had to\
// write it on multiple lines'

// let s = `this is a really long
// string, so long that we had to
// write it on multiple lines`

// //          01234
// let text = 'hello'
// console.log(text[0]) // h
// console.log(text[1]) // e
// console.log(text.charAt(0)) // h

// let s = 'hello' + ' ' + 'world'
// console.log(s) // hello world

// s = 'hello'.concat(' ', 'world')
// console.log(s) // hello world

// Objects
// let contact = {
//     first_name: 'Ronne',
//     last_name: 'Mosley',
//     list_something: ['oranges', 'apples']
// }

// console.log(contact['list_something'][1])

// Loops

// while(i < 5){
//     console.log(i)
//     i += 1
// }

// for(let i=0; i < 5; ++i){
//     console.log(i)
// }

// let s = ['apples', 'oranges', 'pears']

// while(i < s.length){
//     console.log(s[i])
//     i += 1
// }
// console.log(s[0][0])

// for(let i=0; i < s.length; i++){
//     console.log(s[i])
// }

// for(i in s){
//     console.log(s[i])
// }

// let fruits = {
//     'apples': 2,
//     'bananas': 5,
//     'pears': 10,
// }

// for(f in fruits) {
//     console.log(f)
// }

// Arrays
// let nums = [2, 10, 1]

// let fruits = ['apples', 'bananas', 'plums', 'pears', 'cherries']

// fruits[0] = 'cherries'

// console.log(fruits)
// console.log(fruits.length)
// console.log(fruits.includes('apples'))
// console.log(fruits.includes('pears'))
// console.log(fruits.indexOf('pears'))
// fruits.unshift('pineapples')
// fruits.push('melon')
// console.log(fruits)

// fruits.shift()
// console.log(fruits)
// console.log(fruits.join(''))

// console.log(fruits.concat(['strawberries', 'grapes']))
// console.log(fruits.slice(1, 3))
// console.log(fruits.sort())
// console.log(nums.sort((a, b) => a - b))

// nums.sort(function(a, b) {
//     if (a < b) {
//       return -1
//     } else if (a > b) {
//       return 1
//     } else {
//       return 0
//     }
//   })

// Functions
// Classes

// class Animals {
//     constructor(legs){
//         this.legs = legs
//     }
//     move() {
//         if(this.legs > 0) {
//             console.log('walk')
//         } else {
//             console.log('slithers')
//         }
//     }
// }

// class Dog extends Animals {
//     constructor(legs, sound='bark'){
//         super(legs) // invokin parent
//         this.sound = sound
//     }
//     animalcall() {
//         console.log(this.sound)
//     }
//     move() {
//         super.move()
//         console.log('dog moving')
//     }
// }

// let newDog = new Dog(4)

// console.log(newDog.legs)
// newDog.move()
// newDog.animalcall()

// let new_atm = new ATM(5.0, 'RMosley')
// let someBank = new Bank('some bank')
// console.log(new_atm.get_balance())
// console.log(new_atm.get_username())
// console.log(someBank.get_user())

// function Animal(legs) {
//     this.legs = legs || 0
// }

// Animal.prototype.move = function () {
//     if (this.legs < 0) {
//         console.log('walk')
//     } else {
//         console.log('slither')
//     }
// }

// Dog.prototype = Object.create(Animal.prototype)

// function Dog(legs, sound) {
//     Animal.call(this, legs)
//     this.sound = sound || 'ruff'
// }
// Dog.prototype.bark = function () {
//     console.log(this.sound)
// }

// let newDog = new Dog(4)

// console.log(newDog.legs)
// newDog.move()
// newDog.bark()


// console.log(u)


// let i = 0

// let nums = [1, 2, 3, 4, 5, 6, 7, 8]
// for (let i=0; i<nums.length; ++i) {
//     if (nums[i]%2 == 1) {
//         break
//     }
//     console.log(nums[i])
// }


// List
// let nums = [2, 10, 1]

// let fruits = ['apples', 'bananas', 'plums', 'pears', 'cherries']


// fruits[0] = 'cherries'

// console.log(fruits)
// console.log(fruits.length)
// console.log(fruits.includes('apples'))
// console.log(fruits.includes('pears'))
// console.log(fruits.indexOf('pears'))
// fruits.unshift('pineapples')
// fruits.push('melon')
// console.log(fruits)

// fruits.shift()
// console.log(fruits)
// console.log(fruits.join(''))

// console.log(fruits.concat(['strawberries', 'grapes']))
// console.log(fruits.slice(1, 3))
// console.log(fruits.sort())
// console.log(nums.sort((a, b) => a - b))

// nums.sort(function(a, b) {
//     if (a < b) {
//       return -1
//     } else if (a > b) {
//       return 1
//     } else {
//       return 0
//     }
//   })

//   console.log(nums)

// class ATM {
//     constructor(balance=0) {
//       this.balance = balance
//     }
//     get_balance() {
//       return this.balance
//     }
// }

// let new_atm = new ATM(5.0)
// alert(atm.get_balance())

// // using an object
// let atm = {
//   balance: 5.0,
//   get_balance: function() {
//     return this.balance
//   }
// }

// alert(atm.get_balance())

// // Class Inheritance
// class Animal {
//     constructor(legs = 0) {
//         this.legs = legs
//     }

//     move() {
//         if (this.legs > 0) {
//             console.log('walk')
//         } else {
//             console.log('slither')
//         }
//     }
// }
// class Dog extends Animal {
//     constructor(legs = 4, sound = 'ruff') {
//         super(legs) // invoke the parent class's constructor
//         this.sound = sound
//     }

//     bark() {
//         console.log(this.sound)
//     }
    
//     move() { // override the parent method
//       super.move() // call the parent method (optional)
//       console.log('dog moving')
//     }
// }

// let myDog = new Dog(4)

// console.log(myDog.legs) // logs 4
// myDog.move() // logs 'walk', 'dog moving'
// myDog.bark() // logs 'ruff'

// // ES5 Example
// function Animal(legs) {
//     this.legs = legs || 0 // use default value if needed
// }

// Animal.prototype.move = function () {
//     if (this.legs > 0) {
//         console.log('walk')
//     } else {
//         console.log('slither')
//     }
// }

// function Dog(legs, sound) {
//     Animal.call(this, legs) // parent 'constructor'
//     this.sound = sound || 'ruff'
// }

// Dog.prototype = Object.create(Animal.prototype)

// Dog.prototype.bark = function () {
//     console.log(this.sound)
// }

// var myDog = new Dog(4)

// console.log(myDog.legs) // logs 4
// myDog.move() // logs 'walk'
// myDog.bark() // logs 'ruff'