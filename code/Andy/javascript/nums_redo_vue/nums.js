// var app = new Vue({
//     el: '#app',
//     data: { // data object
//         userinput: '', //user key
//         number : 6,




//     },
//     methods: {
//         convertNum: function(){
//            this.number > userinput
//         }
//     },
//     created: function() {

//     }
// })
let app = new Vue({
    // query selector of the html element representing the app
    el: '#app',
    // app data
    // data stored with the app
    // for displaying in the page: {{message}}
    // for getting input from the user: v-model="message"
    // for modifying in methods: this.message
    data: {
        userinput: '',
        result: 0,
        //   return ,
        low_numbers: {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'tweleve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
        },
        tens: {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "nintey",
        },
        hundreds: {

            1: "one hundred",
            2: "two hundred",
            3: "three hundred",
            4: 'four hundred',
            5: 'five hundred',
            6: 'six hundred',
            7: 'seven hundred',
            8: 'eight hundred',
            9: 'nine hundred',
        },


    },
    // app methods
    // can be called from events in the page: v-on:click="method"
    // can be called from other methods: this.method()
    // can be called from outside the app: app.method()
    methods: {
        convert: function (event) {
            let result
            let lastOne
            let user = this.userinput
            // userTwo = user
            console.log(typeof(parseInt(user)), 'user')
            // let result = this.low_numbers[user]
            // this.result = this.result
            this.result = this.low_numbers[user]
            lastOne = user.slice(-1)
            console.log(lastOne, 'last one')
            // 654 : 654/10 = 65.4  /10 = 6.54 how we get the 6 for hundreds digit 
            hundredsDigit = parseInt((user/10)/10) 
            // 654/10 = 65.4 /10 = 6.54 % 10= 
            unitsDigit = parseInt(((user/10)%10)) 
            console.log(unitsDigit, 'units digit') 
            console.log(hundredsDigit, 'testing hundreds digit')
            console.log(user,'testing users')
            console.log(this.low_numbers[user],'testing' )
            console.log(this.low_numbers[lastOne],'testing v2' )
            console.log(this.tens[unitsDigit],'testing v2' )
            console.log(this.hundreds[hundredsDigit],'testing v2' )
            this.userinput = ''
            return result
        },
    },
})

    // created - a lifecycle hook
    // called when the app is created
    // useful for setting up app data

    // tens_digit = number // 10 
    // new_tens = tens_digit % 10
    // ones_digit = number % 10
    // tens_word = ten[new_tens]
    // ones_word = low_numbers[ones_digit]