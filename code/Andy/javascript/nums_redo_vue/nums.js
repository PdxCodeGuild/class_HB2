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
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "nintey",
        },
        hundreds: {

            100: "one hundred",
            200: "two hundred",
            300: "three hundred",
            400: 'four hundred',
            500: 'five hundred',
            600: 'six hundred',
            700: 'seven hundred',
            800: 'eight hundred',
            900: 'nine hundred',
        },


    },
    // app methods
    // can be called from events in the page: v-on:click="method"
    // can be called from other methods: this.method()
    // can be called from outside the app: app.method()
    methods: {
        convert: function (event) {
            let result
            let user = this.userinput
            console.log(user, 'user')
            const expr = user >= 20;
            switch (expr){
                case 'case 1 ':
                    console.log('number greater than 20')
                    break;
            }
            // let result = this.low_numbers[user]
            // this.result = this.result
            this.result = this.low_numbers[user]
            console.log(this.low_numbers[user],'testing' )
            this.userinput = ''
            return result
        },
    },
})

    // created - a lifecycle hook
    // called when the app is created
    // useful for setting up app data
