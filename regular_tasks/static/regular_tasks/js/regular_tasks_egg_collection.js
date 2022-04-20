console.log("Regular tasks egg collection start")
// Extracts the Tray Quantity from Farm Profile in the db

form_data = {};
var traysQuantity;
var total_eggs_laid;
var average_egg_weight;
var saleable_eggs;
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu34.gitpod.io/regular_tasks/trays_quantity')
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
        // if the field is an empty string, set the value = 0
        if (item.value == '') {
            form_data[item.name] = 0;
        }
        else {
            form_data[item.name] = Number(item.value);
        }
        console.log("form_data = " + item.name + ": " + form_data[item.name])
    })
    total_eggs_laid = (form_data['qty_egg_trays'] * traysQuantity) + form_data['qty_egg_singles']
    document.getElementById("qty-total-eggs-laid").innerHTML = total_eggs_laid;
    console.log("total_eggs_laid = " + total_eggs_laid)
    average_egg_weight = (form_data['weight_total_eggs_laid'] / (total_eggs_laid - form_data['qty_eggs_broken']))
    document.getElementById("avg-egg-weight").innerHTML = average_egg_weight;
    console.log("average_egg_weight = " + average_egg_weight);
    saleable_eggs = (total_eggs_laid - (form_data['qty_eggs_damaged'] + form_data['qty_eggs_broken'] + form_data['qty_eggs_personal_use'] + form_data['qty_eggs_given_free']))
    document.getElementById("qty-saleable-eggs").innerHTML = saleable_eggs;
    console.log("saleable_eggs = " + saleable_eggs);
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


// Function to automatically populate a unit of measurement
const measurementUnit = document.getElementById("weights-and-measures-units").value;
$("#unit-of-measurement").html(measurementUnit);


// Feeds Auto-Suggest: Set of functions that auto-suggests feeds from the db once the User begins typing
function setInputTextFeed(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('feed-suggestions-list').style.display = "none";
}
function showSuggestionsFeeds(value, labelId) {
    if (value.length) {
        // displaySelectLabel(labelId)
        let suggestions = '';
        FEEDS.filter(item => item.feed_type.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            console.log("Feed Type :", item.feed_type);
            suggestions += `<div onclick="setInputTextFeed('feed-type', '${item.feed_type}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.feed_type}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('feed-suggestions-list').innerHTML = suggestions;
            document.getElementById('feed-suggestions-list').style.display = "block";
        } else {
            document.getElementById('feed-suggestions-list').style.display = "none";
        }
    } else {
        // hideSelectLabel(labelId)
        document.getElementById('feed-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu40.gitpod.io/regular_tasks/get_feeds')
.then(response => response.json())
.then(data => {
    console.log("Fetch feed type fn fires");
    FEEDS = data.feeds;
    console.log("Feed Types :", FEEDS);
});
