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

  // HCC Section: Ensures at least one quantity is indicated
  function validateQtys(){
      if( document.getElementById('total-birds').value == null){
        document.getElementById("bird-qty-warning").textContent = 
          "Please provide at least one quantity for Hens, Chicks or Cocks.";
        return false;
      }
  }

  // Sales Methods & Units Function to ensure at least one checkbox is checked
  // in each section before next page can be loaded
  function injectHref(){
      var salesMethods = null;
      var salesUnits = null;
      if( document.getElementById('roadside-check').checked == true ||
          document.getElementById('markets-check').checked == true ||
          document.getElementById('deliveries-check').checked == true ||
          document.getElementById('collections-check').checked == true) {
          salesMethods = true;
          } else {
            salesMethods = false
          }
          console.log("sales-methods" + salesMethods);

      if( document.getElementById('single-eggs-check').checked == true ||
          document.getElementById('half-dozen-carton-check').checked == true ||
          document.getElementById('dozen-carton-check').checked == true ||
          document.getElementById('trays-check').checked == true ){
          salesUnits = true;
          } else {
            salesUnits = false
          }
          console.log("sales-units" + salesUnits);

      if (salesMethods == true && salesUnits == true){
          window.location.href = "{% url 'onboard_stock' %}"; //{% url 'onboard_stock' %});
          } else {
            document.getElementById('sales-unit-method-warning').textContent = 
            "Please select at least one option each from Sales Methods and Sales Units";
          }
      }

      
    $('#myModal').on('shown.bs.modal', function () {
      $('#myInput').trigger('focus')
    })