$(document).ready(function(){
    
    avgUnitOfMeasurement()
    
});


form_data = {};
var traysQuantity;
var total_eggs_laid;
var average_egg_weight;
var saleable_eggs;
var qtys_single_eggs;
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu45.gitpod.io/regular_tasks/trays_quantity')
.then(response => response.json())
.then(data => {
    traysQuantity = data.trays_quantity;
    // console.log("traysQuantity = " + traysQuantity);
    doCalculations();
});


function doCalculations() {
    // console.log("traysQuantity again = " + traysQuantity)

    // I don't think this is required any longer
    // if (traysQuantity == null) {
    //     $('input[name=qty_egg_trays]').parent().hide();
    // }
    document.querySelectorAll('input').forEach(item => {
        form_data[item.name] = Number(item.value);
        // console.log("form_data type = " + item.name + ": " + typeof(form_data[item.name]));
    })
    
    total_eggs_laid = (form_data['qty_egg_trays'] * traysQuantity) + form_data['qty_egg_singles']
    document.getElementById("qty-total-eggs-laid").innerHTML = total_eggs_laid;
    // console.log("total_eggs_laid = " + total_eggs_laid)
    average_egg_weight = (form_data['weight_total_eggs_laid'] / (total_eggs_laid - form_data['qty_eggs_broken']))
    measurementUnit = document.getElementById("weights-and-measures-units").value;
    // If there is no value, "--" is displayed as the average egg weight
    if (isNaN(average_egg_weight) || (form_data['weight_total_eggs_laid'] == '')) {
        document.getElementById("avg-egg-weight").innerHTML = "--";
    }
    // If the User selects kg, the avg egg weight is displayed in grammes
    else if (measurementUnit === "kg"){
        document.getElementById("avg-egg-weight").innerHTML = (average_egg_weight*1000).toFixed(0);
    }
    // If the User selects lb, the avg egg weight is displayed in ounces
    else if (measurementUnit === "lb"){
        document.getElementById("avg-egg-weight").innerHTML = (average_egg_weight*16).toFixed(2);
    }
    // If the User selects oz, the avg egg weight is displayed in ounces to 2 decimal places
    else if (measurementUnit === "oz"){
        document.getElementById("avg-egg-weight").innerHTML = (average_egg_weight).toFixed(2);
    }
    // If the User selects g, the avg egg weight is displayed in g to 0 decimal places
    else {
        document.getElementById("avg-egg-weight").innerHTML = average_egg_weight.toFixed(0);
    }
    saleable_eggs = (total_eggs_laid - (form_data['qty_eggs_damaged'] + form_data['qty_eggs_broken'] + form_data['qty_eggs_personal_use'] + form_data['qty_eggs_given_free']))  
    // console.log("saleable_eggs = " + saleable_eggs);
    document.getElementById("qty-saleable-eggs").innerHTML = saleable_eggs;

    showHideAdvance ();
};


// EGG WEIGHT UNIT OF MEASUREMENT: Fn to automatically display unit of measurement as per User's default
// or based on their selection from a dropdown, converting it to either g or oz (because eggs are light)
var measurementUnit;
function avgUnitOfMeasurement() {
    doCalculations();
    measurementUnit = document.getElementById("weights-and-measures-units").value;
    if (measurementUnit === "kg"){
        $("#unit-of-measurement").html("g");
    }
    else if (measurementUnit === "lb"){
        $("#unit-of-measurement").html("oz");
    }
    else {
        $("#unit-of-measurement").html(measurementUnit);
    }
}
// Allows the Unit of Measurement dropdown to call the above function
$("#weights-and-measures-units").on('change', function(){
    avgUnitOfMeasurement();
});


function validate(event) {
    // console.log("Validate function");
    // console.log("form_data = " + form_data);
    for (item in form_data) {
        // console.log(item + form_data[item])
    }
    if (total_eggs_laid == 0 ) {                  
        document.getElementById("warning-section-text").textContent =
        "Please enter a quantity for the number of trays collected and/or the number of single eggs collected";
        // stop form submission
        event.preventDefault();
                    
    } 
    else if (saleable_eggs < 0) {
        document.getElementById("warning-section-text").textContent =
        "Hmmm, something's not right. The total number of eggs damaged, broken, used personally and/or given away free can't be higher than the quantity of eggs laid.";
        // stop form submission
        event.preventDefault();
    } 
    else {
        document.getElementById("warning-section-text").textContent = "";
    }
}


// Extracts the Qty of laying hens in a flock from Farm Profile in the db. This allows us to decide 
// whether to display trays and singles inputs, or just singles. The latter is set at less than 12 hens.
let hensQuantity;
let trays_input_div = document.getElementById('trays_input_div');
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu45.gitpod.io/flock_management/hens_quantity')
.then(response => response.json())
.then(data => {
    hensQuantity = data.hens_quantity;

    if (hensQuantity < 12) {
        trays_input_div.style.display = 'none';
    }
});


// Show/Hide Advanced: This is a type of validation in that it prevents the User from seeing the Advanced section,
// and therefore from adding data (which results in negative and Nan's).
let advancedSection = document.getElementById('egg-collection-advanced-section');
function showHideAdvance () {
    console.log("total_eggs_laid :" + total_eggs_laid);
    if (total_eggs_laid > 0) {
        advancedSection.style.display = 'block';
    }
    else {
        advancedSection.style.display = 'none';
    }
}

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
