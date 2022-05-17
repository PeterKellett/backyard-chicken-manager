console.log("health_and_welfare_supplements.js");

fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu45.gitpod.io/health_and_welfare/get_supplements')
.then(response => response.json())
.then(data => {
    console.log("Fetch supplement type fn fires");
    SUPPLEMENTS = data.supplements;
    console.log("Supplements Types :", SUPPLEMENTS);
});

// Feeds Auto-Suggest: Set of functions that auto-suggests feeds from the db once the User begins typing
function setInputTextSupplement(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('supplement-suggestions-list').style.display = "none";
}

function showSuggestionsSupplements(value, labelId) {
    if (value.length) {
        let suggestions = '';
        SUPPLEMENTS.filter(item => item.supplement_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            console.log("Supplement Type :", item.supplement_name);
            suggestions += `<div onclick="setInputTextSupplement('supplement-name', '${item.supplement_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.supplement_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('supplement-suggestions-list').innerHTML = suggestions;
            document.getElementById('supplement-suggestions-list').style.display = "block";
        } else {
            document.getElementById('supplement-suggestions-list').style.display = "none";
        }
    } else {
        // hideSelectLabel(labelId)
        document.getElementById('supplement-suggestions-list').style.display = "none";
    }
}

$("#hens-row").hide();
$("#chicks-row").hide();
$("#cocks-row").hide();
var hens;
var chicks;
var cocks;

function applyFlockQuantities() {
    console.log("applyFlockQuantities")
    var element = document.getElementById("flock-name");
    var selected = element.selectedIndex;
    flock_hens = Number(element.options[selected].dataset.hens); 
    flock_chicks = Number(element.options[selected].dataset.chicks); 
    flock_cocks = Number(element.options[selected].dataset.cocks); 
    console.log("hens = " + flock_hens);
    console.log("chicks = " + flock_chicks);
    console.log("cocks = " + flock_cocks);
    if (flock_hens > 0) {
        $("#hens-row").show();
        if ($("#all-hens-check").is(':checked')) {
            $("#qty-hens").val(flock_hens);
        }
    }
    else {
        $("#hens-row").hide();
    }
    if (flock_chicks > 0) {
        $("#chicks-row").show();
        if ($("#all-chicks-check").is(':checked')) {
            $("#qty-chicks").val(flock_chicks);
        }
    }
    else {
        $("#chicks-row").hide();
    }
    if (flock_cocks > 0) {
        $("#cocks-row").show();
        if ($("#all-cocks-check").is(':checked')) {
            $("#qty-cocks").val(flock_cocks);
        }
    }
    else {
        $("#cocks-row").hide();
    }
    doCalculations();
}

$("#all-hens-check").change(function() {
    if (this.checked) {
        console.log("checked")
        $("#qty-hens").val(flock_hens);
        // document.getElementById("qty-hens").value = hens;
    }
    else {
        console.log("unchecked")
        $("#qty-hens").val(0);
    }
    doCalculations();
});

$("#all-chicks-check").change(function() {
    if (this.checked) {
        console.log("checked")
        $("#qty-chicks").val(flock_chicks);
    }
    else {
        console.log("unchecked")
        $("#qty-chicks").val(0);
    }
    doCalculations();
});

$("#all-cocks-check").change(function() {
    if (this.checked) {
        console.log("checked");
        $("#qty-cocks").val(flock_cocks);
    }
    else {
        console.log("unchecked")
        $("#qty-cocks").val(0);
    }
    doCalculations();
});

function doCalculations() {
    console.log("doCalculations")
    form_data = {};
    document.querySelectorAll('input').forEach(item => {
        form_data[item.name] = Number(item.value);
        console.log("item.name = " + item.name)
        console.log("item.value = " + item.value)
    })
    var dose_per_bird = form_data['dosage_amount'] / (form_data['qty_hens'] + form_data['qty_chicks'] + form_data['qty_cocks']);
    console.log("dose_per_bird = " + dose_per_bird)
    if (isNaN(dose_per_bird) || dose_per_bird == Infinity || (form_data['dosage_amount'] == '')) {
        $("#dose-per-bird").html("--- ");
    }
    else {
        $("#dose-per-bird").html(dose_per_bird.toFixed(2));
    }
}