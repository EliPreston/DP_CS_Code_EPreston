
var uNames = []
var pWords = []

// Populate lists with JSON file
// Requires using something called a fetch
// A fetch is used to tell a web page to go and get something
// Takes time and keepd code running
// BIG IDEA: Asynchronus processing and the funny things that happen
// Keep in mind promises ~ A fetch returns a promise


var url = "https://raw.githubusercontent.com/EliPreston/DP_CS_Code_EPreston/master/Bad%20Auth%20Example/logindata.json"

fetch(url, {})
.then(response => response.json())
.then(result => {

    for (i = 0; i < result.length; i = i + 1) {
        uNames.push(result[i]["uID"])
        pWords.push(result[i]["password"])
    }
    // console.log(uNames, pWords)
})





// Step 1: Get form
var loginForm = document.getElementById("login-form");
var mLogin = document.getElementById("modal-login")
var homePage = document.getElementById("home")
var landingPage = document.getElementById("landing")

// Step 2: Event listener
loginForm.addEventListener("submit", function(e) {

    // Stops form from reloading the page
    e.preventDefault() 

    email = document.getElementById("login-email").value
    password = document.getElementById("login-password").value

    result = checkLogin(email,password)
    console.log(result)
    if (result == true) {
        homePage.style.display = "block"
        navLanding.style.display = "block"
        landingPage.style.display = "none"
    }

    // console.log(email)
    $(mLogin).modal("close")
})




///////////////////////////////////////////////
function checkLogin(u,p) {

    for(i = 0; i < uNames.length; i++) {
        if (u === uNames[i]) {
            if (pWords[i] === p) {
                return true;
            }
            else {
                return false;
            }
        }   
    }
    return false;
}


function logout() {
    homePage.style.display = "none"
    navLanding.style.display = "none"
    landingPage.style.display = "block"
}