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

    // DATE: Automatically have date fields display the current date based on the User's location
    // Partially taken from: https://stackoverflow.com/questions/67659091/why-i-am-getting-this-warning-message-does-not-conform-to-the-required-format
    var date = document.getElementById("todays-date");
    console.log("date = " + date)
    if (date != null) {
        document.getElementById("todays-date").addEventListener("load", dateToday);
        function dateToday() {
            const todayDate = new Date(); 
            const formatDate = todayDate.getDate() < 10 ? `0${todayDate.getDate()}`:todayDate.getDate();
            const formatMonth = todayDate.getMonth() < 10 ? `0${todayDate.getMonth()+1}`: todayDate.getMonth()+1;
            const formattedDate = [todayDate.getFullYear(), formatMonth, formatDate].join('-');
            document.getElementById('todays-date').value = formattedDate;
        }
        dateToday()
        // DATE MAX: Ensures Users cannot choose a date that is later than the current date.
        // Taken from: https://stackoverflow.com/questions/32378590/set-date-input-fields-max-date-to-today
        document.getElementById('todays-date').max = new Date().toISOString().split("T")[0];
    }
    

    // Call hccTotal function on page load
    // hccTotal();
    
    
})

// Makes a modal display on a page when User lands on it. Used for when a User initially
// lands on a page and we require some data. Once the data has been provided, it must
// not display again. Function needs to be updated for the latter.
// Taken from https://www.tutorialrepublic.com/faq/how-to-launch-bootstrap-modal-on-page-load.php
$(document).ready(function(){
    $("#page-setup-modal").modal('show');
});


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
// Show Hide 3: This fn displays a div when an input is changed and the value is greater than 1
// First used in Egg Collection so that Advanced Section only displays if the user inputs a collected quantity
// $(document).ready(function () {
//     $('div.show-on-change').hide();

//     //show it when the input changes
//     $('input[class="change-to-show"]').on('change', function () {
//         if ($(this).value > 1) {
//             $('div.show-on-change').fadeIn();
//         } else {
//             $('div.show-on-change').hide();
//         }
//     });
// });


// Sales Methods & Units Function to ensure at least one checkbox
// is checked in each section before next page can be loaded
// Taken from (kind of): https://www.javascripttutorial.net/javascript-dom/javascript-form/
function injectHref() {
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


// Floating Input Labels using ID: Display floating label on Select/Dropdown inputs when a selection is made
function displaySelectLabel(id) {
    console.log("Float Label fn fires");
    document.getElementById(id).style.display = "block";
    if (id === 'select-recipient-label') {
        checkAndToggleHCCDivVisibility();
    }
}

// function hideSelectLabel(id) {
//     document.getElementById(id).style.display = "none";
// }

function checkAndToggleHCCDivVisibility() {
    const dropdown = document.getElementById('recipients')
    if (dropdown.options[dropdown.selectedIndex].id === "individual-birds") {
        document.getElementById('hcc-container-div').style.display = "block";
    } else {
        document.getElementById('hcc-container-div').style.display = "none";
    }
}





