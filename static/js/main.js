$(document).ready(function(){
    console.log("Document ready!")
  });


  // Show Password. Taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
  function showPasswordFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }