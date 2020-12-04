var firebaseConfig = {
    apiKey: "AIzaSyDaF1Opv15ml7D15izgxous4CK58mHsP7A",
    authDomain: "dpcs-firebasedemo-42949.firebaseapp.com",
    databaseURL: "https://dpcs-firebasedemo-42949.firebaseio.com",
    projectId: "dpcs-firebasedemo-42949",
    storageBucket: "dpcs-firebasedemo-42949.appspot.com",
    messagingSenderId: "313542347468",
    appId: "1:313542347468:web:587da2cdc612a2eea91069",
    measurementId: "G-F3PS8N9NWG",
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();

  var database = firebase.database();

  function writeUserData(userId, name, email) {
    var userId = document.getElementById("uId").value;
    var name = document.getElementById("uName").value;
    var email = document.getElementById("email").value;

    database.ref("users/" + userId).set({
      // "users/" references the node of users in firebase, this can be changed, or anything can be put in the "" as
      // long as it matches to the firebase node/branch it is referencing
      username: name,
      email: email,
    });
    console.log("Success");
  }

  // writeUserData("02", "Bob", "bob@test.com");