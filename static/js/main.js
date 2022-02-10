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

  // Calculation to sum total number of birds in HCC section
  function hccTotal(){
      var totalHens = document.querySelector('input[name=hens-qty]').value;
      var totalChicks = document.querySelector('input[name=chicks-qty]').value;
      var totalCocks = document.querySelector('input[name=cocks-qty]').value;
      var total = Number(totalHens) + Number(totalChicks) + Number(totalCocks);
      document.getElementById("total-birds").textContent = total;
  }

  // HCC Section: Ensures at least one input is selected when there are multiple options
  function validateQtys(){
      if( document.getElementById('total-birds').value == null){
        document.getElementById("bird-qty-warning").textContent = "Please provide at least one quantity for Hens, Chicks or Cocks.";
        return false;
      }
  }

  function validateMethods(){
      if( document.querySelector('input[class=sales-methods]').checked = false)(
        console.log("False")
      )
  }