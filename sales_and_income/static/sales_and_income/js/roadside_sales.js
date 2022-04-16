$(document).ready(function() {
    console.log("Roadside sales Document ready!");
    // Show Hide 3: This set of functions allows a field(s) to be displayed when another
    // field has been completed. The first function hides all of the relevenat fields.
    // The second function allows the fields hidden in teh 1st fn to be shown.
    console.log("PK")
    $('div.single_egg_price').hide();
    $('div.half_dozen_eggs_price').hide();
    $('div.ten_eggs_price').hide();
    $('div.dozen_eggs_price').hide();
    $('div.trays_of_eggs_price').hide();

    var initial_data = {}
    document.querySelectorAll('input').forEach(item => {
        console.log("item.name = " + item.name)
        console.log("item.value = " + item.value)
        // item.addEventListener('oninput', doCalculations())
        // Depending on the values in the prices form hide/show respective sales/stock fields
        if (item.value > 0) {
            $(`div.${item.name}`).fadeIn();
        } 
        // Save the input field names and values of each form field to the dictionary initial_data
        initial_data[item.name] = item.value ; 
        console.log("initial_data = " + initial_data)  
    });    
    // Show/Hide singles fields dependent on in_stock field
    if (initial_data['qty_single_eggs_in_stock'] > 0) {
        $('input[name=qty_single_eggs_in_stock]').parent().hide();
        $('input[name=qty_single_eggs_added]').parent().show();
        $('input[name=qty_single_eggs_remaining]').parent().show();
        document.querySelector('input[name=qty_single_eggs_remaining]').required = true;
        document.querySelector('input[name=qty_single_eggs_added]').required = true;
    }
    else {
        $('input[name=qty_single_eggs_in_stock]').parent().show();
        $('input[name=qty_single_eggs_added]').parent().hide();
        $('input[name=qty_single_eggs_remaining]').parent().hide();
    }
    // Show/Hide 1/2 dozen in stock
    if (initial_data['qty_half_dozen_egg_boxes_in_stock'] > 0) {
        $('input[name=qty_half_dozen_egg_boxes_in_stock]').parent().hide();
        $('input[name=qty_half_dozen_egg_boxes_added]').parent().show();
        $('input[name=qty_half_dozen_egg_boxes_remaining]').parent().show();
        document.querySelector('input[name=qty_half_dozen_egg_boxes_remaining]').required = true;
        document.querySelector('input[name=qty_half_dozen_egg_boxes_added]').required = true;
    } else {
        $('input[name=qty_half_dozen_egg_boxes_in_stock]').parent().show();
        $('input[name=qty_half_dozen_egg_boxes_added]').parent().hide();
        $('input[name=qty_half_dozen_egg_boxes_remaining]').parent().hide();
    }
    // Show/Hide 10's in stock
    if (initial_data['qty_ten_egg_boxes_in_stock'] > 0) {
        $('input[name=qty_ten_egg_boxes_in_stock]').parent().hide();
        $('input[name=qty_ten_egg_boxes_added]').parent().show();
        $('input[name=qty_ten_egg_boxes_remaining]').parent().show();
        document.querySelector('input[name=qty_ten_egg_boxes_remaining]').required = true;
        document.querySelector('input[name=qty_ten_egg_boxes_added]').required = true;
    } else {
        $('input[name=qty_ten_egg_boxes_in_stock]').parent().show();
        $('input[name=qty_ten_egg_boxes_added]').parent().hide();
        $('input[name=qty_ten_egg_boxes_remaining]').parent().hide();
    }
    // Show/Hide Dozen in stock
    if (initial_data['qty_dozen_egg_boxes_in_stock'] > 0) {
        $('input[name=qty_dozen_egg_boxes_in_stock]').parent().hide();
        $('input[name=qty_dozen_egg_boxes_added]').parent().show();
        $('input[name=qty_dozen_egg_boxes_remaining]').parent().show();
        document.querySelector('input[name=qty_dozen_egg_boxes_remaining]').required = true;
        document.querySelector('input[name=qty_dozen_egg_boxes_added]').required = true;
    } else {;
        $('input[name=qty_dozen_egg_boxes_in_stock]').parent().show();
        $('input[name=qty_dozen_egg_boxes_added]').parent().hide();
        $('input[name=qty_dozen_egg_boxes_remaining]').parent().hide();
    }
    // Show/Hide trays in stock
    if (initial_data['qty_trays_eggs_in_stock'] > 0) {
        $('input[name=qty_trays_eggs_in_stock]').parent().hide();
        $('input[name=qty_trays_eggs_added]').parent().show();
        $('input[name=qty_trays_eggs_remaining]').parent().show();
        document.querySelector('input[name=qty_trays_eggs_remaining]').required = true;
        document.querySelector('input[name=qty_trays_eggs_added]').required = true;
    } else {
        $('input[name=qty_trays_eggs_in_stock]').parent().show();
        $('input[name=qty_trays_eggs_added]').parent().hide();
        $('input[name=qty_trays_eggs_remaining]').parent().hide();
    }
});
function doCalculations() {
    var form_data = {}
    document.querySelectorAll('input').forEach(item => {
        // Save the input field names and values of each form field to the dictionary form_data
        form_data[item.name] = item.value;
        // Depending on the values in the prices form hide/show respective sales/stock fields
        if (item.value > 0) {
            $(`div.${item.name}`).fadeIn();
        } 
    });    

    if (form_data['qty_single_eggs_remaining'] == '') {
        form_data['qty_single_eggs_remaining'] = form_data['qty_single_eggs_in_stock'];
    }
    if (form_data['qty_half_dozen_egg_boxes_remaining'] == '') {
        form_data['qty_half_dozen_egg_boxes_remaining'] = form_data['qty_half_dozen_egg_boxes_in_stock'];
    }
    if (form_data['qty_ten_egg_boxes_remaining'] == '') {
        form_data['qty_ten_egg_boxes_remaining'] = form_data['qty_ten_egg_boxes_in_stock'];
    }
    if (form_data['qty_dozen_egg_boxes_remaining'] == '') {
        form_data['qty_dozen_egg_boxes_remaining'] = form_data['qty_dozen_egg_boxes_in_stock'];
    }
    if (form_data['qty_trays_eggs_remaining'] == '') {
        form_data['qty_trays_eggs_remaining'] = form_data['qty_trays_eggs_in_stock'];
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
