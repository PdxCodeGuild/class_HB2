const initApp = () => {
    const currentValueElem = document.querySelector('.currentvalue');
    const previousValueElem = document.querySelector('.previousvalue');
    
    let itemArray = [];
    const equatArray = [];
    let newNumFlag = false;
// being able to populate buttons on calc screen
    const inputbuttons = document.querySelectorAll('.number');
    inputbuttons.forEach(button =>{
        button.addEventListener("click", event => {
            //new charachter, any new one that is added the event could be chaneged to button cause thats where it really coming from but doesnt matter
            const newInput = event.target.textContent;
            // knowing when to switch from a new number
            if (newNumFlag){
                currentValueElem.value = newInput;
                // adding new num 
                newNumFlag = false;
            } else{ 
                currentValueElem.value = 
                //once the operator or anthing other than a number is pressed the 0 comes back to start the second part
                    currentValueElem.value == 0 
                        ? newInput // just to get the number and not 07. ?: those can be considered as if and else statements/ so if true set to new input then else would start after:
                        : `${currentValueElem.value}${newInput}`; // concatnating a new a diff way 
            }

        });
         
    });
    const operateButton = document.querySelectorAll('.operator');
    operateButton.forEach(button =>{
        button.addEventListener('click', event =>{
            //showing equals
            if(newNumFlag){
                previousValueElem.textContent = ''
                itemArray = [];
            }
            const newOperator = event.target.textContent
            currentVal = currentValueElem.value

            // num needs to be first if no number cant preform operation. if item array has no lenth/ basically saying if 0 and then + wont do stuff
            if (!itemArray.length && currentVal == 0 ) return
            //new equation has no length
            if (!itemArray.length){
                itemArray.push(currentVal, newOperator)
                previousValueElem.textContent = `${currentVal} ${newOperator}`;
                 // being done so when an op is pressed it doesnt append the next num to the previous
                return newNumFlag = true
            }
             //completing equations
            if (itemArray.length) {
                itemArray.push(currentVal) //thrid elem
                const equationObj = {
                   //storing numbers not strings
                    numOne: parseFloat(itemArray[0]),
                    //current value is num two
                    numTwo: parseFloat(currentVal),
                    // thats the second element in the array
                    op: itemArray[1]

                    
                }
                equatArray.push(equationObj); // history for equations
                const equationStr = 
                    `${equationObj['numOne']}
                     ${equationObj['op']}
                     ${equationObj['numTwo']}`;

            
                 const newValue = calculate(equationStr, currentValueElem);
                 
                 previousValueElem.textContent = 
                    `${newValue} ${newOperator}`;

                    // start new equation
                    itemArray = [newValue, newOperator];
                    newNumFlag = true
                    console.log(equatArray); 


            }
        });
    });
    // equal sign 
    const equalsButton = document.querySelector('.equal-sign');
    equalsButton.addEventListener('click',() =>{
        const currentVal= currentValueElem.value;
        let equationObj;
        // letting user press equals more than once and continuing to increase #
        if (!itemArray.length && equatArray.length){
            const lastEqua = equatArray[equatArray.length - 1 ]; // getting last stuff
            equationObj = {
                numOne : parseFloat(currentVal),
                numTwo: lastEqua.numTwo,
                op: lastEqua.op 
            }
        }else if (!itemArray.length){ //saying it'll work even though it doesnt have a history and works past first option 
            return currentVal
        }else {
            itemArray.push(currentVal);
            equationObj={
                numOne:parseFloat(itemArray[0]),
                numTwo: parseFloat(currentVal),
                op: itemArray[1]
            }
        }

        equatArray.push(equationObj)

        const equationStr= 
        `${equationObj['numOne']} ${equationObj['op']} ${equationObj['numTwo']}`;
        calculate(equationStr, currentValueElem);

        previousValueElem.textContent= `${equationStr}=`

        newNumFlag = true;
        itemArray = [];
        console.log(equatArray);
    });

   //setting up all clear 
    const allClearButton = document.querySelectorAll('.all-clear');
    allClearButton.forEach(button =>{
        button.addEventListener('click', (event)=>{
            currentValueElem.value =0; 
            // targeting all clear to get 0
            if (event.target.classList.contains('all-clear')){
                previousValueElem.textContent = ''
                 itemArray=[];//clearing items that have been put within it 
                
            }

        });

        

    });
    
    
};
// fires when all html docs have been completley parsed and all deferred scripts. doesnt wait for everthing to load 
document.addEventListener('DOMContentLoaded', initApp);

const calculate = (equation, currentValueElem) => {
    const regex = /(^[*/=])|(\s)/g; //  /(^) means if it starts with \s means removing white space
    equation.replace(regex,''); // from params
    const divByZero = /(\/0)/.test(equation)
    if (divByZero) return currentValueElem.value = 0; // catching the division by 0 and making it 0
    return currentValueElem.value = eval(equation); // return the value
}