// function add(a, b) {


//     // var A = a
//     // var B = b
//     // console.log(A+B)

    
//     console.log(a+b)
// }

// add(3,4)









// function functionOne(x) { 
//     console.log(x); 
// }

// functionOne(10)




// function functionTwo(var1, passedFunction) {
//     passedFunction(var1);	
    	
// }


// functionTwo(10, functionOne);




// function functionThree(var1, var2, var3, functionParam) {
//     functionParam(var1);
//     functionParam(var2);
//     functionParam(var3);

// }

// functionThree(1,2,3,functionOne)

// 
// 
// 


function multiplyPrint(x) {
    console.log(x*3);
}

function dividePrint(x) {
    console.log(x/2)
}

function functionFour(var1, variableFunction1, variableFunction2) {
    variableFunction1(var1);
    variableFunction2(var1);


}


// multiplyPrint(4)
// dividePrint(4)
functionFour(4, multiplyPrint, dividePrint)

