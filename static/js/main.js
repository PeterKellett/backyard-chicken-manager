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
    // hccTotal();
    
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
        form_data[item.name] = item.value    
    });    
    // for (k in form_data) {
    //     console.log("k ", k)
    //     console.log("v ", form_data[k])
    // }
    if (form_data['qty_single_eggs_remaining'] == '') {
        form_data['qty_single_eggs_remaining'] = form_data['qty_single_eggs_in_stock']
    }
    if (form_data['qty_half_dozen_egg_boxes_remaining'] == '') {
        form_data['qty_half_dozen_egg_boxes_remaining'] = form_data['qty_half_dozen_egg_boxes_in_stock']
    }
    if (form_data['qty_ten_egg_boxes_remaining'] == '') {
        form_data['qty_ten_egg_boxes_remaining'] = form_data['qty_ten_egg_boxes_in_stock']
    }
    if (form_data['qty_dozen_egg_boxes_remaining'] == '') {
        form_data['qty_dozen_egg_boxes_remaining'] = form_data['qty_dozen_egg_boxes_in_stock']
    }
    if (form_data['qty_trays_eggs_remaining'] == '') {
        form_data['qty_trays_eggs_remaining'] = form_data['qty_trays_eggs_in_stock']
    }
    var value_of_single_eggs_sold = (form_data['single_egg_price'] * (form_data['qty_single_eggs_in_stock'] - form_data['qty_single_eggs_remaining']));
    var value_of_half_dozen_egg_boxes_sold = (form_data['half_dozen_eggs_price'] * (form_data['qty_half_dozen_egg_boxes_in_stock'] - form_data['qty_half_dozen_egg_boxes_remaining']));
    var value_of_ten_eggs_sold = (form_data['ten_eggs_price'] * (form_data['qty_ten_egg_boxes_in_stock'] - form_data['qty_ten_egg_boxes_remaining']));
    var value_of_dozen_eggs_sold = (form_data['dozen_eggs_price'] * (form_data['qty_dozen_egg_boxes_in_stock'] - form_data['qty_dozen_egg_boxes_remaining']));
    var value_of_trays_eggs_sold = (form_data['trays_of_eggs_price'] * (form_data['qty_trays_eggs_in_stock'] - form_data['qty_trays_eggs_remaining']));

    var total_value = Number(value_of_single_eggs_sold) + Number(value_of_half_dozen_egg_boxes_sold) + Number(value_of_ten_eggs_sold) + Number(value_of_dozen_eggs_sold) + Number(value_of_trays_eggs_sold) - (Number(form_data['losses_eggs_roadside']) * form_data['single_egg_price']);
    document.getElementById("eggs-sold-value").innerHTML = total_value;
    var income_difference = form_data['income'] - total_value;
    document.getElementById("income-deficit").innerHTML = income_difference;
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
