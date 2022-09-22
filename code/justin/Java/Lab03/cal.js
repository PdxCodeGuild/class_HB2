let screen = document.querySelector(".calculator-screen");
let keys = document.querySelector(".calculator-keys");
let input = null;
let nums = [];
let a = null; let b= null;let c= null;
let math = null;

function algo(x,y,z){
    let answer = null
    if(y =='+'){
        answer = parseFloat(a, 10) + parseFloat(c, 10);
    }
    else if(y == '-'){
        answer = parseFloat(a, 10) - parseFloat(c, 10);
    }
    else if(y == '*'){
        answer = parseFloat(a, 10) * parseFloat(c, 10);
    }
    else if(y == '/'){
        answer = parseFloat(a, 10) / parseFloat(c, 10);
    }
    console.log(x,y,z+' '+'='+' '+answer);
    answer = Math.round(answer * 10000)/10000
    return answer
};
function update(x){
    screen.value = x;
}


keys.addEventListener("click", e => {
    if(e.target.className == "all-clear"){
        a = null, b = null, c = null;
        update(0);
    }
    else if(e.target.className == 'equal-sign'){
        if(a != null && b != null && c != null){
            answer = algo(a,b,c);
            update(answer);
            a = answer, b = null, c = null;
            console.log(a+b+c);
            console.log(answer);
        }
    }
    else if(e.target.className == "operator"){
        if(a == null){
            a = 0
        };
        b = e.target.value;
        console.log(b);        
    }
    else{
        input = e.target.value;
        if(b == null){
            if(a == null){
                if(input == '.'){
                    a = '0.';
                    update(a);
                }
                else{a = input;
                update(a);
                console.log(a);
                }
            }
            else if(a != null){
                if(input == '.'){
                    a = a.toString()
                    if(a.includes('.')){
                        update(a);
                    }
                    else{
                        a += input;
                        update(a);
                    }
                
                }
                else{
                    a += input;
                    update(a);
                    console.log(a);
                    }
                    
            }
        }
        else if(a != null && b != null){
            if(c == null){
                if(input == '.'){
                    c = '0.';
                    update(c);
                }
                else{c = input;
                update(c);
                console.log(c)}
            }
            else if(c != null){
                if(c.includes('.') == true && input == '.'){
                    update(c);
                }
                else{
                c += input;
                update(c);
                console.log(c);}
            }
        }
        
    // if(a == null){
    //    a = parseInt(input, 10);
    // }
    // else if(b != null && c == null){
    //     c = parseInt(input, 10);
    //     if(b=='+'){
    //         math = a + c;}
    //     else if(b=='-'){
    //         math = a - c;
    //     }
    //     else if(b=='*'){
    //         math = a * c;
    //     }
    //     console.log(math)
      

        
        // console.log(algo())
    }
}
    // algo();
)



