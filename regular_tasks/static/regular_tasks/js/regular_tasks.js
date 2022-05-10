$(document).ready(function() {
    console.log("Regular tasks egg collection Document ready!!")

    

});
console.log("Regular tasks egg collection JS start")

// Egg Collection - Variables
var total_eggs_laid = 0;
var damaged_eggs;
var broken_eggs;
var eggs_personal_use;
var eggs_given_free;
var saleable_eggs;
var total_weight;
var total_nonsaleable_eggs;
// let traysQuantity;
let hensQuantity;
let egg_qty_2col_div = document.getElementById('egg-qty-2col-div');
let egg_qty_1col_div = document.getElementById('egg-qty-1col-div');


// Extracts the Qty of laying hens in a flock from Farm Profile in the db
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu44.gitpod.io/flock_management/hens_quantity')
.then(response => response.json())
.then(data => {
    hensQuantity = data.hens_quantity;
    console.log("Hens Quantity = " + hensQuantity)

    if (hensQuantity < 12) {
        egg_qty_2col_div.style.display = 'none';
        egg_qty_1col_div.style.display = 'block';
        console.log("Less than 12 " + hensQuantity);
    }
    else {
        egg_qty_2col_div.style.display = 'block';
        egg_qty_1col_div.style.display = 'none';
        console.log("more than 12 " + hensQuantity);
    }

});


// Extracts the Tray Quantity from Farm Profile in the db
// fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu44.gitpod.io/regular_tasks/trays_quantity')
// .then(response => response.json())
// .then(data => {
//     traysQuantity = data.trays_quantity;
//     console.log("traysQuantity = " + traysQuantity)
// });

// Egg Collection - Eggs Laid Calculation: Calculation to sum total number of eggs laid
// document.querySelectorAll('.egg-collection-qty-input').forEach(item => {
//     item.addEventListener('keyup', event => {
//         // send request to latest no of trays
//         console.log("querySelectorAll('.egg-collection-qty-input')")
//         var totalTrays = document.getElementById('qty-egg-trays').value;
//         var totalTraysQty = totalTrays * traysQuantity;
//         var totalSingles = document.getElementById('qty-egg-singles').value;
//         total_eggs_laid = Number(totalTraysQty) + Number(totalSingles);
//         document.getElementById("qty-total-eggs-laid").innerHTML = total_eggs_laid;
//     })
// });

// Egg Collection - Saleable Eggs Calculation: Calculation to get total saleable eggs
// document.querySelectorAll('.saleable-eggs-input').forEach(item => {
//     item.addEventListener('keyup', event => {
//         console.log("querySelectorAll('.saleable-eggs-input')")
//         damaged_eggs = document.getElementById('qty-eggs-damaged').value;
//         broken_eggs = document.getElementById('qty-eggs-broken').value;
//         eggs_personal_use = document.getElementById('qty-eggs-personal-use').value;
//         eggs_given_free = document.getElementById('qty-eggs-given-free').value;
//         saleable_eggs = Number(total_eggs_laid) - (Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free));
//         document.getElementById('qty-saleable-eggs').innerHTML = Number(saleable_eggs);
//     })
// });

// Egg Collection - Weight Calculation: Calculation to average weight of eggs laid
// document.querySelectorAll('.average-weight-input').forEach(item => {
//     item.addEventListener('keyup', event => {
//         var weighable_eggs = Number(total_eggs_laid) - Number(broken_eggs);
//         total_weight = document.getElementById('weight-total-eggs-laid').value;
//         var average_egg_weight = Number(total_weight) / Number(weighable_eggs);
//         document.getElementById("avg-egg-weight").innerHTML = average_egg_weight;
//     })
// });

// Egg Collection - Validation: Prevents form being submitted if 
// User hasn't provided a quantity of laid eggs and/or
// if non-saleable eggs qty is greater than total of non-saleable elements
// document.getElementById("save-button").onclick = function() {preventFormSubmission()};
// function preventFormSubmission() {
//         var totalTrays = document.getElementById('qty-egg-trays').value;
//         var totalTraysQty = totalTrays * traysQuantity;
//         var totalSingles = document.getElementById('qty-egg-singles').value;
//         total_eggs_laid = Number(totalTraysQty) + Number(totalSingles);
//         total_nonsaleable_eggs = Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free);

//         if (total_eggs_laid == 0 ) {
//                 document.getElementById("submit-form").addEventListener('submit', (event) => {
//                     document.getElementById("warning-section-text").textContent =
//                     "Please enter a quantity for the number of trays collected and/or the number of single eggs collected";
//                     // stop form submission
//                     event.preventDefault();
//             })
//         } else if (total_nonsaleable_eggs > total_eggs_laid) {
//                 document.getElementById("submit-form").addEventListener('submit', (event) => {
//                     document.getElementById("warning-section-text").textContent =
//                     "Hmmm, something's not right. The total number of eggs damaged, broken, used personally and/or given away free can't be higher than the quantity of eggs laid.";
//                     // stop form submission
//                     event.preventDefault();
//             })
//         } else {
//             document.getElementById("submit-form").submit();
//         }
//     };

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
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/regular_tasks/get_feeds')
.then(response => response.json())
.then(data => {
    console.log("Fetch feed type fn fires");
    FEEDS = data.feeds;
    console.log("Feed Types :", FEEDS);
});
