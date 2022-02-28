// Egg Collection - Variables
var total_eggs_laid = 0;
var damaged_eggs;
var broken_eggs;
var eggs_personal_use;
var eggs_given_free;
var saleable_eggs;
var total_weight;
var total_nonsaleable_eggs;

// Egg Collection - Eggs Laid Calculation: Calculation to sum total number of eggs laid
function testFunction(){
    console.log("Test Function")
};

document.querySelectorAll('.egg-collection-qty-input').forEach(item => {
    item.addEventListener('keyup', event => {
        console.log("Eggs Laid Calc Fires");
        var totalTrays = document.getElementById('qty-trays').value;
        // trayQty needs to be updated to dynamically take in number of eggs per tray
        var trayQty = 30;
        var totalTraysQty = totalTrays * trayQty;
        var totalSingles = document.getElementById('qty-singles').value;
        total_eggs_laid = Number(totalTraysQty) + Number(totalSingles);
        document.getElementById("total-eggs-laid").value = Number(total_eggs_laid);
    })
});

// Egg Collection - Saleable Eggs Calculation: Calculation to get total saleable eggs
document.querySelectorAll('.saleable-eggs-input').forEach(item => {
    item.addEventListener('keyup', event => {
        console.log("Saleable Eggs Calc Fires");
        damaged_eggs = document.getElementById('eggs-damaged').value;
        broken_eggs = document.getElementById('eggs-broken').value;
        eggs_personal_use = document.getElementById('eggs-personal-use').value;
        eggs_given_free = document.getElementById('eggs-given-free').value;
        saleable_eggs = Number(total_eggs_laid) - (Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free));
        console.log("total_eggs_laid: " + total_eggs_laid);
        document.getElementById('qty-saleable-eggs').value = Number(saleable_eggs);
    })
});

// Egg Collection - Weight Calculation: Calculation to average weight of eggs laid
document.querySelectorAll('.average-weight-input').forEach(item => {
    item.addEventListener('keyup', event => {
        console.log("Average Egg Weight Calc Fires");
        var weighable_eggs = Number(total_eggs_laid) - Number(broken_eggs);
        console.log("Weighable Eggs: " + weighable_eggs);
        total_weight = document.getElementById('total-weight-laid').value;
        var average_egg_weight = Number(total_weight) / Number(weighable_eggs);
        var average_egg_weight_metric = Math.ceil(average_egg_weight * 1000);
        document.getElementById("average-egg-weight").value = Number(average_egg_weight_metric);
    })
});

// Egg Collection - Warning: Displays if there are more non-saleable eggs than eggs laid
document.querySelectorAll('.saleable-eggs-input').forEach(item => {
    item.addEventListener('keyup', event => {
        total_nonsaleable_eggs = Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free);
        console.log("total_nonsaleable_eggs: " + total_nonsaleable_eggs)
        console.log("total_eggs_laid: " + total_eggs_laid)

        if (total_nonsaleable_eggs > total_eggs_laid) {
                document.getElementById("warning-section-text").textContent =
                "Hmmm, something's not right. The total for eggs damaged, broken, used personally and/or given away free can't be higher than the quantity of eggs laid.";
            };
        })
    });

// Egg Collection - Validation: Prevents form being submitted if 
// non-saleable eggs qty is greater than total of non-saleable elements
document.getElementById("save-button").onclick = function() {preventFormSubmission()};
function preventFormSubmission() {
        total_nonsaleable_eggs = Number(damaged_eggs) + Number(broken_eggs) + Number(eggs_personal_use) + Number(eggs_given_free);
        if (total_nonsaleable_eggs > total_eggs_laid || total_eggs_laid == 0 ) {
                document.getElementById("submit-form").addEventListener('submit', (event) => {
                    document.getElementById("warning-section-text").textContent =
                    "Egg collection quantity can't be 0 or the total for eggs damaged, broken, used personally and/or given away free can't be higher than the quantity of eggs laid.";
                    // stop form submission
                    event.preventDefault();
            });
        } else {
            document.getElementById("submit-form").submit();
            console.log("Right Calc");
        }
    };