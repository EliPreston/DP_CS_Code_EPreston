





var uNames = ["user1", "user2", "user3"]
var pWords = ["pword1", "pword2", "pword3"]

function checkLogin(u,p) {
    
 
    var u = document.getElementById("username").value;
    // console.log(u)

    var p = document.getElementById("password").value;
    // console.log(p);

    for(i = 0; i < uNames.length; i++) {
        if (u === uNames[i]) {
            if (pWords[i] === p) {
                alert("Logged in.")
                return true;
            }
            else {
                console.log("Error")
                alert("Incorrect login info.")
                return false;
            }
        }   
    }
    alert("User does not exist.")
    return false;
}

// var --> a global variable
// let --> only works inside the scope of the block statement
// const -->  


// function checkLogin(u,p) {

//     uvaild = false;
//     pvalid = false;
//     index = 0;

//     // linear search loop, checking if u exists
//     for(i = 0; i < uNames.length; i = i + 1) {

//         // JS == vs ===
//         // == --> compares only the value "1" == 1 --> True
//         // === --> compares value and type "1" === 1 --> False
//         if (uNames[i] === u) {
//             uvalid = true;
//             index = i;
//         }
//     }
    
//     if (pWords[index] == p) {
//         pvalid = true
//     }

//     if (uvalid === true && pvalid == true) {
//         return true;
//     }
//     return false

// }
