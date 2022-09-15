let ones = {
    0:'zero',
    1 : 'one',
    2 :'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
}
let teens = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
let tens = {10:'ten',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

function n2p(){
    event.preventDefault();
    let number = document.getElementById('number').value;
    let algo = null
    if(number <= 10 && number >=0){
        algo = ones[number]
    }
    else if(number >=11 && number <=19){
        algo = teens[number]
    }
    else if(number >=20 && number <= 99){
        let ten = Math.floor(number/10)*10;
        let one = number % 10;
        if(one==0){
            algo = tens[ten]
        }
    
        else{
        algo = tens[ten] + '-' + ones[one]
        }
    }
    else{
        algo = 'number too high or low, enter 0-99, sorry'
    }
    let answer = document.getElementById('result')
    answer.innerHTML = `<h1>${algo}</h1>`
}