// 4556737586899855

function validator(number){
    // let number = save_num()
    let card_list = []
    let every_other_num = []
    let number_string = number.split('') // split method puts it in a array
    for (let i=0; i<number_string.length; i++){
        let convert_num = parseInt(number_string[i])
        card_list.push(convert_num)
        
        // number_string.push(convert_num)
        // console.log(number_string[i])
        // console.log(typeof(convert_num), 'line 10')
        // console.log(card_list)
        // console.log(card_list.slice(0,-1),'last' )
        // let  = new_card_list = card_list.slice(0,-1, 'last')
        // console.log(new_card_list)
    }
    let check_digit = card_list.pop()
    console.log(check_digit, 'check dog')
    let new_card_list =  card_list.reverse()
    console.log(new_card_list, 'new card')
    for (let x=0; x<new_card_list.length; x++) {
    //    console.log(i,'testing 22')
    //    console.log(new_card_list[i], "line 23")
        // console.log(new_card_list[i]*2, 'multipying')
        if(x%2 === 0){
            // console.log(new_card_list[i]*2,'line 26')
            every_other_num.push(new_card_list[x]*2)
            
        } else if(x%2 === 1){
            every_other_num.push(new_card_list[x])
        }
    }
    for (let x=0; x<every_other_num.length; x++){
        if (every_other_num[x]>9){
            every_other_num[x]=every_other_num[x]-9
            every_other_num.push[x]
        }else if (every_other_num[x]!==9){
            every_other_num.push[x]
        }
    }
    
    let total_sum = []
    let running_total = 0 // not resetting when outside 
    for( let x=0; x<every_other_num.length; x++){
        running_total = every_other_num[x]+ running_total
        // running_total += every_other_num[x] same thing just different 
        //1 =           x[1]=1                 +0 
        //9=            x[2]=8                 +1
        //18=           x[3]=9                 +9 
        console.log(running_total,'running total')
        total_sum.push(running_total)
    }
    // console.log(total_sum.pop(), 'confirming 55')
     eighty_five = total_sum.pop()
     console.log(eighty_five,'popped 85')
    
    let second_digit = eighty_five
    console.log(second_digit.toString(), 'second digit')
    console.log(typeof(second_digit.toString(), 'second digit'))
    let converted_num_str = second_digit.toString()
    console.log(converted_num_str.split(''), 'should be 5')
    let sum_values_array = converted_num_str.split('')
    console.log(sum_values_array)
    // console.log(sum_values_array.pop())
    let last_number = sum_values_array.pop()
    console.log(last_number)
    // console.log(every_other_num,'line 44')

    // if ()

    // if ()
//   console.log(new_card_list, 'doubler numbers')  
    // let credit_card_num = parseInt(number)
    // credit_card_num.split(',')
    // for (let x=1; x<16; ++x) {
    //     credit_card_num.push(x)
    // } // the ++x is incrementing by 1 going to the next number 
    return check_digit == last_number
    // return typeof(credit_card_num)
}
// alert('testing')

console.log(validator("4556737586899855"))


// if (true){
//     // console.log('is True')
// }
// if (5 == 5){
//     // console.log('5=5')
// }
// let check_digit = '5' 
// let last_number = "5"
// if (check_digit === last_number){
//     console.log('compaing two equal digits')
// } else{
// console.log('these arent equal')
// }
// let checkNum;
// let returnObject = document.getElementById("return");
// let cardNumsRaw;
// function convertstring(