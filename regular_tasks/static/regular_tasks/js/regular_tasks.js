// Egg Collection - Variables
var trayQty = "{{ trays_quantity|safe }}";
var total_eggs_laid = 0;
var damaged_eggs;
var broken_eggs;
var eggs_personal_use;
var eggs_given_free;
var saleable_eggs;
var total_weight;
var total_nonsaleable_eggs;

// Egg Collection - Eggs Laid Calculation: Calculation to sum total number of eggs laid
document.querySelectorAll('.egg-collection-qty-input').forEach(item => {
    item.addEventListener('keyup', event => {
        console.log("Eggs Laid Calc Fires Now");
        var totalTrays = document.getElementById('qty-egg-trays').value;
        console.log("totalTrays", totalTrays);
        var totalTraysQty = totalTrays * trayQty;
        console.log("totalTraysQty", totalTraysQty);
        var totalSingles = document.getElementById('qty-egg-singles').value;
        console.log("totalSingles", totalSingles);
        total_eggs_laid = Number(totalTraysQty) + Number(totalSingles);
        console.log("total_eggs_laid", total_eggs_laid);
        document.getElementById("qty-total-eggs-laid").innerHTML = total_eggs_laid;
    })
});

// Egg Collection - Saleable Eggs Calculation: Calculation to get total saleable eggs
document.querySelectorAll('.saleable-eggs-input').forEach(item => {
    item.addEventListener('keyup', event => {
        console.log("Saleable Eggs Calc Fires");
        damaged_eggs = document.getElementById('qty-eggs-damaged').value;
        broken_eggs = document.getElementById('qty-eggs-broken').value;
        eggs_personal_use = document.getElementById('qty-eggs-personal-use').value;
        eggs_given_free = document.getElementById('qty-eggs-given-free').value;
        saleable_eggs = Number(total_eggs_laid) - (Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free));
        console.log("qty_total_eggs_laid: " + total_eggs_laid);
        console.log("saleable_eggs: " + saleable_eggs);
        document.getElementById('qty-saleable-eggs').value = Number(saleable_eggs);
    })
});

// Egg Collection - Weight Calculation: Calculation to average weight of eggs laid
document.querySelectorAll('.average-weight-input').forEach(item => {
    item.addEventListener('keyup', event => {
        console.log("Average Egg Weight Calc Fires");
        var weighable_eggs = Number(total_eggs_laid) - Number(broken_eggs);
        console.log("Weighable Eggs: " + weighable_eggs);
        total_weight = document.getElementById('weight-total-eggs-laid').value;
        console.log("total_weight: " + total_weight);
        var average_egg_weight = Number(total_weight) / Number(weighable_eggs);
        console.log("average_egg_weight: " + average_egg_weight);
        var average_egg_weight_metric = Math.ceil(average_egg_weight * 1000);
        document.getElementById("avg-egg-weight").value = Number(average_egg_weight_metric);
    })
});

// Egg Collection - Validation: Prevents form being submitted if 
// User hasn't provided a quantity or laid eggs and/or
// if non-saleable eggs qty is greater than total of non-saleable elements
document.getElementById("save-button").onclick = function() {preventFormSubmission()};
function preventFormSubmission() {
        console.log("preventFormSubmission Fires");
        var totalTrays = document.getElementById('qty-egg-trays').value;
        var totalTraysQty = totalTrays * trayQty;
        var totalSingles = document.getElementById('qty-egg-singles').value;
        total_eggs_laid = Number(totalTraysQty) + Number(totalSingles);
        total_nonsaleable_eggs = Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free);

        if (total_eggs_laid == 0 ) {
                document.getElementById("submit-form").addEventListener('submit', (event) => {
                    document.getElementById("warning-section-text").textContent =
                    "Please enter a quantity for the number of trays collected and/or the number of single eggs collected";
                    // stop form submission
                    event.preventDefault();
            })
        } else if (total_nonsaleable_eggs > total_eggs_laid) {
                document.getElementById("submit-form").addEventListener('submit', (event) => {
                    document.getElementById("warning-section-text").textContent =
                    "Hmmm, something's not right. The total number of eggs damaged, broken, used personally and/or given away free can't be higher than the quantity of eggs laid.";
                    // stop form submission
                    event.preventDefault();
            })
        } else {
            document.getElementById("submit-form").submit();
            console.log("Right Calc");
        }
    };
