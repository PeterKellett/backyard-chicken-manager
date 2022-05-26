console.log("health_and_welfare_vaccines.js");

// Vaccines Auto-Suggest: Set of functions that auto-suggests vaccines in the db once the User begins typing
function setInputTextVaccine(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('vaccine-suggestions-list').style.display = "none";
}
function showSuggestionsVaccines(value) {
    if (value.length) {
        let suggestions = '';
        VACCINES.filter(item => item.vaccine_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            suggestions += `<div onclick="setInputTextVaccine('vaccine-name', '${item.vaccine_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.vaccine_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('vaccine-suggestions-list').innerHTML = suggestions;
            document.getElementById('vaccine-suggestions-list').style.display = "block";
        } else {
            document.getElementById('vaccine-suggestions-list').style.display = "none";
        }
    } else {
        document.getElementById('vaccine-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellet-backyardchi-6r0pf5jpjxn.ws-eu45.gitpod.io/health_and_welfare/get_vaccines')
.then(response => response.json())
.then(data => {
    VACCINES = data.vaccines;
});

// Viruses Auto-Suggest: Set of functions that auto-suggests viruses in the db once the User begins typing
function setInputTextVirus(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('virus-suggestions-list').style.display = "none";
}
function showSuggestionsViruses(value) {
    if (value.length) {
        let suggestions = '';
        VIRUSES.filter(item => item.virus_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            suggestions += `<div onclick="setInputTextVirus('virus-protected-against', '${item.virus_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.virus_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('virus-suggestions-list').innerHTML = suggestions;
            document.getElementById('virus-suggestions-list').style.display = "block";
        } else {
            document.getElementById('virus-suggestions-list').style.display = "none";
        }
    } else {
        document.getElementById('virus-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellet-backyardchi-6r0pf5jpjxn.ws-eu45.gitpod.io/health_and_welfare/get_viruses')
.then(response => response.json())
.then(data => {
    VIRUSES = data.viruses;
});

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
        // console.log("item.name = " + item.name)
        // console.log("item.value = " + item.value)
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
