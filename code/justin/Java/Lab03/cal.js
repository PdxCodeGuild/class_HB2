let screen = document.querySelector(".calculator-screen");
let keys = document.querySelector(".calculator-keys");
let input = null;
let nums = [];
let a = null; let b= null;let c= null;
let math = null;
function algo(){
    let answer =`${a}${b}${c}`;
    return answer
}


keys.addEventListener("click", e => {
    if(e.target.className == "all-clear"){
        a = null, b = null, c = null;
        function update(){
            screen.value = 0
        };
        update();
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
                a = parseInt(input, 10);
            }
            else if(a != null && b == null){
                a = a + input;
                console.log(a)
            }
        }
        function update(){
        screen.value = input
    };
    update();
    console.log(input);
    if(a == null){
       a = parseInt(input, 10);
    }
    else if(b != null && c == null){
        c = parseInt(input, 10);
        if(b=='+'){
            math = a + c;}
        else if(b=='-'){
            math = a - c;
        }
        else if(b=='*'){
            math = a * c;
        }
        console.log(math)
      

        
        // console.log(algo())
    }
}
    // algo();
})



