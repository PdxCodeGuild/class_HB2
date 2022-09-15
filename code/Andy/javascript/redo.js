// 4556737586899855

function validator(number){
    // let number = save_num()
    let card_list = []
    let number_string = number.split('') // split method puts it in a array
    for (let i=0; i<number_string.length; i++){
            let convert_num = parseInt(number_string[i])
            card_list.push(convert_num)

            // number_string.push(convert_num)
            // console.log(number_string[i])
            // console.log(typeof(convert_num), 'line 10')
            console.log(card_list)
            console.log(card_list.slice(0,-1, 'last'), )
            // console.log(card_list.reverse('reverse'))

    }

    
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