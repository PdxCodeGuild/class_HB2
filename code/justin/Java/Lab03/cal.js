let screen = document.querySelector(".calculator-screen");
let keys = document.querySelector(".calculator-keys");
let input = null;
let nums = [];
let a = null; let b= null;let c= null;
function algo(){
    let answer =`${a}${b}${c}`;
    return answer
}


keys.addEventListener("click", e => {
    if(e.target.className == "operator"){
       b = e.target.value;
        console.log(b);        
    }
    else{
        input = e.target.value;
    function update(){
        screen.value = input
    };
    update();
    console.log(input);
    if(a == null){
       a = parseInt(input, 10);
    }
    else{
        c = parseInt(input, 10);
        if(b=='+'){
            add = a + c;
            a = add;
            function added(){
                screen.value = a
            };
            added();
            console.log(add)

        }
        // console.log(algo())
    }
}
    // algo();
})



