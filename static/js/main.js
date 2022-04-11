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
    document.getElementById("todays-date").addEventListener("load", dateToday);
    function dateToday() {
        const todayDate = new Date(); 
        const formatDate = todayDate.getDate() < 10 ? `0${todayDate.getDate()}`:todayDate.getDate();
        const formatMonth = todayDate.getMonth() < 10 ? `0${todayDate.getMonth()+1}`: todayDate.getMonth()+1;
        const formattedDate = [todayDate.getFullYear(), formatMonth, formatDate].join('-');
        document.getElementById('todays-date').value = formattedDate;
    }
    dateToday()

    // Call hccTotal function on page load
    // hccTotal();
    
    
})

// $(function() {
//     console.log("Date fn 2 fires");
//     $('#todays-date').datepicker();
//     $('#todays-date').datepicker('setDate', new Date());
// });

// Makes a modal display on a page when User lands on it. Used for when a User initially
// lands on a page and we require some data. Once the data has been provided, it must
// not display again. Function needs to be updated for the latter.
// Taken from https://www.tutorialrepublic.com/faq/how-to-launch-bootstrap-modal-on-page-load.php
$(document).ready(function(){
    console.log("Function fires for modal")
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


// Show Hide 3: This set of functions allows a field(s) to be displayed when another
// field has been completed. The first function hides all of the relevenat fields.
// The second function allows the fields hidden in teh 1st fn to be shown.
$(document).ready(function () {
    $('div.single_egg_price').hide();
    $('div.half_dozen_eggs_price').hide();
    $('div.ten_eggs_price').hide();
    $('div.dozen_eggs_price').hide();
    $('div.trays_of_eggs_price').hide();
    // singles
    var qty_single_eggs_in_stock = document.getElementsByName('qty_single_eggs_in_stock');
    var qty_half_dozen_egg_boxes_in_stock = document.getElementsByName('qty_half_dozen_egg_boxes_in_stock');
    var qty_ten_egg_boxes_in_stock = document.getElementsByName('qty_ten_egg_boxes_in_stock');
    var qty_dozen_egg_boxes_in_stock = document.getElementsByName('qty_dozen_egg_boxes_in_stock');
    var qty_trays_eggs_in_stock = document.getElementsByName('qty_trays_eggs_in_stock');
    // singles in stock
    if (qty_single_eggs_in_stock[0].value > 0) {
        $('input[name=qty_single_eggs_in_stock]').parent().hide();
        $('input[name=qty_single_eggs_added]').parent().show()
        $('input[name=qty_single_eggs_remaining]').parent().show()
    }
    else {
        $('input[name=qty_single_eggs_in_stock]').parent().show();
        $('input[name=qty_single_eggs_added]').parent().hide()
        $('input[name=qty_single_eggs_remaining]').parent().hide()
    }
    // 1/2 dozen in stock
    if (qty_half_dozen_egg_boxes_in_stock[0].value > 0) {
        $('input[name=qty_half_dozen_egg_boxes_in_stock]').parent().hide()
        $('input[name=qty_half_dozen_egg_boxes_added]').parent().show()
        $('input[name=qty_half_dozen_egg_boxes_remaining]').parent().show()
    } else {
        $('input[name=qty_half_dozen_egg_boxes_in_stock]').parent().show()
        $('input[name=qty_half_dozen_egg_boxes_added]').parent().hide()
        $('input[name=qty_half_dozen_egg_boxes_remaining]').parent().hide()
    }
    // 10's in stock
    if (qty_ten_egg_boxes_in_stock[0].value > 0) {
        $('input[name=qty_ten_egg_boxes_in_stock]').parent().hide()
        $('input[name=qty_ten_egg_boxes_added]').parent().show()
        $('input[name=qty_ten_egg_boxes_remaining]').parent().show()
    } else {
        $('input[name=qty_ten_egg_boxes_in_stock]').parent().show()
        $('input[name=qty_ten_egg_boxes_added]').parent().hide()
        $('input[name=qty_ten_egg_boxes_remaining]').parent().hide()
    }
    // Dozen in stock
    if (qty_dozen_egg_boxes_in_stock[0].value > 0) {
        $('input[name=qty_dozen_egg_boxes_in_stock]').parent().hide()
        $('input[name=qty_dozen_egg_boxes_added]').parent().show()
        $('input[name=qty_dozen_egg_boxes_remaining]').parent().show()
    } else {
        $('input[name=qty_dozen_egg_boxes_in_stock]').parent().show()
        $('input[name=qty_dozen_egg_boxes_added]').parent().hide()
        $('input[name=qty_dozen_egg_boxes_remaining]').parent().hide()
    }
    // trays in stock
    if (qty_trays_eggs_in_stock[0].value > 0) {
        $('input[name=qty_trays_eggs_in_stock]').parent().hide()
        $('input[name=qty_trays_eggs_added]').parent().show()
        $('input[name=qty_trays_eggs_remaining]').parent().show()
    } else {
        $('input[name=qty_trays_eggs_in_stock]').parent().show()
        $('input[name=qty_trays_eggs_added]').parent().hide()
        $('input[name=qty_trays_eggs_remaining]').parent().hide()
    }
    doCalculations();
}); 
function doCalculations() {
    console.log("doCalculations")
    var form_data = {}
    document.querySelectorAll('input').forEach(item => {
        // item.addEventListener('oninput', doCalculations())
        // Depending on the values in the prices form hide/show respective sales/stock fields
        if (item.value > 0) {
            $(`div.${item.name}`).fadeIn();
        } else {
            $(`div.${item.name}`).hide();
        }    
        // Save the input field names and values of each form field to the dictionary form_data
        form_data[item.name] = Number(item.value)    
    });    
    // for (k in form_data) {
    //     console.log("k ", k)
    //     console.log("v ", form_data[k])
    // }
    var value_of_single_eggs_sold = (form_data['single_egg_price'] * (form_data['qty_single_eggs_in_stock'] - form_data['qty_single_eggs_remaining']));
    console.log("value_of_single_eggs_sold = " + value_of_single_eggs_sold)

    var value_of_half_dozen_egg_boxes_sold = (form_data['half_dozen_eggs_price'] * (form_data['qty_half_dozen_egg_boxes_in_stock'] - form_data['qty_half_dozen_egg_boxes_remaining']));
    console.log("value_of_half_dozen_egg_boxes_sold = " + value_of_half_dozen_egg_boxes_sold)

    var value_of_ten_eggs_sold = (form_data['ten_eggs_price'] * (form_data['qty_ten_egg_boxes_in_stock'] - form_data['qty_ten_egg_boxes_remaining']));
    console.log("value_of_ten_eggs_sold = " + value_of_ten_eggs_sold)
    
    var value_of_dozen_eggs_sold = (form_data['dozen_eggs_price'] * (form_data['qty_dozen_egg_boxes_in_stock'] - form_data['qty_dozen_egg_boxes_remaining']));
    console.log("value_of_dozen_eggs_sold = " + value_of_dozen_eggs_sold)

    var value_of_trays_eggs_sold = (form_data['trays_of_eggs_price'] * (form_data['qty_trays_eggs_in_stock'] - form_data['qty_trays_eggs_remaining']));
    console.log("value_of_trays_eggs_sold = " + value_of_trays_eggs_sold)

    var total_value = value_of_single_eggs_sold + value_of_half_dozen_egg_boxes_sold + value_of_ten_eggs_sold + value_of_dozen_eggs_sold + value_of_trays_eggs_sold;
    console.log("total_value = " + total_value)
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
function displaySelectLabel(id) {
    console.log("displaySelectLabel Fires", id);
    document.getElementById(id).style.display = "block";
    if (id==='select-recipient-label') {
        checkAndToggleHCCDivVisibility();
    }
}

function hideSelectLabel(id) {
    document.getElementById(id).style.display = "none";
}

function checkAndToggleHCCDivVisibility() {
    const dropdown = document.getElementById('recipients')
    if (dropdown.options[dropdown.selectedIndex].id === "individual-birds") {
        document.getElementById('hcc-container-div').style.display = "block";
    } else {
        document.getElementById('hcc-container-div').style.display = "none";
    }
}

function setInputText(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('medicine-suggestions-list').style.display = "none";
}

function showSuggestions(value, labelId) {
    if (value.length) {
        displaySelectLabel(labelId)
        let suggestions = '';
        MEDICINES.filter(item => item.medicine_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            suggestions += `<div onclick="setInputText('medicine-name', '${item.medicine_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.medicine_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('medicine-suggestions-list').innerHTML = suggestions;
            document.getElementById('medicine-suggestions-list').style.display = "block";
        } else {
            document.getElementById('medicine-suggestions-list').style.display = "none";
        }
    } else {
        hideSelectLabel(labelId)
        document.getElementById('medicine-suggestions-list').style.display = "none";
    }
}

fetch('https://8000-peterkellett-backyardchi-ajalkdyk1o7.ws-eu39.gitpod.io/health_and_welfare/get_medicines')
.then(response => response.json())
.then(data => {
    console.log({data});
    MEDICINES = data.medicines;
});
// Floating Input Labels using Class: Display floating label on Select inputs when a selection is made
function displaySelectLabel2() {
    console.log("displaySelectLabel2 Fires");
    document.querySelectorAll('.select-input-label').style.display = "block";
}
