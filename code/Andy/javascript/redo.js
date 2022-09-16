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
        console.log(card_list.slice(0,-1, 'last'), )
        let  = new_card_list = card_list.slice(0,-1, 'last')
        console.log(new_card_list)
        new_card_list.reverse()
        console.log(new_card_list)
    }
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
    

console.log(every_other_num,'line 44')
//   console.log(new_card_list, 'doubler numbers')  
    // let credit_card_num = parseInt(number)
    // credit_card_num.split(',')
    // for (let x=1; x<16; ++x) {
    //     credit_card_num.push(x)
    // } // the ++x is incrementing by 1 going to the next number 
    return number_string
    // return typeof(credit_card_num)
}
// alert('testing')

console.log(validator("4556737586899855"))

// let checkNum;
// let returnObject = document.getElementById("return");
// let cardNumsRaw;
// function convertstring(