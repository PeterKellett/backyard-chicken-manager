$(document).ready(function () {
    console.log("Document ready!");
  
    // Show Password. Taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
    function showPasswordFunction() {
        var x = document.getElementById("password");
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
    }

    // Call hccTotal function on page load
    hccTotal();
    
})


// Show Hide 1: Function to display additional field(s) or content when a checkbox is checked
// Taken from http://jsfiddle.net/TrueBlueAussie/DLQY9/1/
$(document).ready(function () {
    $('div.show-on-click').hide();

    //show it when the checkbox is clicked
    $('input[class="click-to-show"]').on('click', function () {
        if ($(this).prop('checked')) {
            $('div.show-on-click').fadeIn();
        } else {
            $('div.show-on-click').hide();
        }
    });
});
// Show Hide 2: This fn allows an existing div to be hidden and replaced by whatever div
// is displayed Show Hide 1 above. First used on Tray Qty checkbox in onboarding_produce.
$(document).ready(function () {
    $('input[class="click-to-show"]').on('click', function () {
        if ($(this).prop('checked')) {
            $('div.hide-on-click').hide();;
        } else {
            $('div.hide-on-click').fadeIn();
        }
    });
});


// Show Hide 3: This set of functions allows a field(s) to be displayed when another
// field has been completed. The first function hides all of the relevenat fields.
// The second function allows the fields hidden in teh 1st fn to be shown.
$(document).ready(function () {
    $('div.single-egg-price-section').hide();
    $('div.half-dozen-eggs-price-section').hide();
    $('div.ten-eggs-price-section').hide();
    $('div.dozen-eggs-price-section').hide();
    $('div.trays-of-eggs-price-section').hide();
});
function showHideInputFields(value, className) {
    if(value.length > 0) {
        $(`div.${className}`).fadeIn();
    } else {
        $(`div.${className}`).hide();
    }
}


// Sales Methods & Units Function to ensure at least one checkbox
// is checked in each section before next page can be loaded
// Taken from (kind of): https://www.javascripttutorial.net/javascript-dom/javascript-form/
function injectHref() {
    console.log("Inject Href");
    var salesMethods = null;
    var salesUnits = null;
    if (document.getElementById('roadside-check').checked == true ||
        document.getElementById('markets-check').checked == true ||
        document.getElementById('deliveries-check').checked == true ||
        document.getElementById('collections-check').checked == true) {
        salesMethods = true;
    } else {
        salesMethods = false
    }

    if (document.getElementById('single-eggs-check').checked == true ||
        document.getElementById('half-dozen-carton-check').checked == true ||
        document.getElementById('dozen-carton-check').checked == true ||
        document.getElementById('trays-check').checked == true) {
        salesUnits = true;
    } else {
        salesUnits = false
    }

    if (salesMethods == true && salesUnits == true){
        document.getElementById("submit-form").submit();
    } else {
        document.getElementById('warning-section-text').textContent =
            "Please select at least one option each from Sales Methods and Sales Units";
            document.getElementById("submit-form").addEventListener('submit', (event) => {
                // stop form submission
                event.preventDefault();
            });
        }
    }


// Function to make textarea height to expand based on amopunt of text added by the user.
// Taken from https://www.techiedelight.com/automatically-resize-textarea-height-javascript/
$(document).ready(function() {
    $('textarea').on('keyup keypress', function() {
        $(this).height(0);
        $(this).height(this.scrollHeight);
    });
});


// Floating Input Labels using ID: Display floating label on Select inputs when a selection is made
function displaySelectLabel() {
    console.log("displaySelectLabel Fires");
    document.getElementById('select-input-label').style.display = "block";
}
// Floating Input Labels using Class: Display floating label on Select inputs when a selection is made
function displaySelectLabel2() {
    console.log("displaySelectLabel2 Fires");
    document.querySelectorAll('.select-input-label').style.display = "block";
}
