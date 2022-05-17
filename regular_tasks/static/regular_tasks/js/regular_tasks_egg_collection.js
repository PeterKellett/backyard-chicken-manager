console.log("Regular tasks egg collection start")
// Extracts the Tray Quantity from Farm Profile in the db

form_data = {};
var traysQuantity;
var total_eggs_laid;
var average_egg_weight;
var saleable_eggs;
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu45.gitpod.io/regular_tasks/trays_quantity')
.then(response => response.json())
.then(data => {
    traysQuantity = data.trays_quantity;
    console.log("traysQuantity = " + traysQuantity);
    doCalculations();
});

function doCalculations() {
    console.log("traysQuantity again = " + traysQuantity)
    if (traysQuantity == null) {
        $('input[name=qty_egg_trays]').parent().hide();
    }
    document.querySelectorAll('input').forEach(item => {
        form_data[item.name] = Number(item.value);
        console.log("form_data = " + item.name + ": " + typeof(form_data[item.name]))
    })
    
    total_eggs_laid = (form_data['qty_egg_trays'] * traysQuantity) + form_data['qty_egg_singles']
    document.getElementById("qty-total-eggs-laid").innerHTML = total_eggs_laid;
    console.log("total_eggs_laid = " + typeof(total_eggs_laid))
    average_egg_weight = (form_data['weight_total_eggs_laid'] / (total_eggs_laid - form_data['qty_eggs_broken']))
    if (isNaN(average_egg_weight) || (form_data['weight_total_eggs_laid'] == '')) {
        document.getElementById("avg-egg-weight").innerHTML = "--- ";
    }
    else {
        document.getElementById("avg-egg-weight").innerHTML = average_egg_weight.toFixed(2);
    }
    saleable_eggs = (total_eggs_laid - (form_data['qty_eggs_damaged'] + form_data['qty_eggs_broken'] + form_data['qty_eggs_personal_use'] + form_data['qty_eggs_given_free']))  
    console.log("saleable_eggs = " + saleable_eggs);
    document.getElementById("qty-saleable-eggs").innerHTML = saleable_eggs;
}

function validate(event) {
    console.log("Validate function");
    console.log("form_data = " + form_data);
    for (item in form_data) {
        console.log(item + form_data[item])
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
