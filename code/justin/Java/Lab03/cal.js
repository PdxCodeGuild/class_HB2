let screen = document.querySelector(".calculator-screen");
let keys = document.querySelector(".calculator-keys");
let input = null;


keys.addEventListener("click", e => {
    if(e.target.className == "operator"){
        console.log('this is a operator')
    }
    else{
        input = e.target.value;
    function update(){
        screen.value = input
    };
    update();
    console.log(input)}
})



