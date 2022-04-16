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

    // DATE: Automatically have date fields display the current date based on the User's location
    // Partially taken from: https://stackoverflow.com/questions/67659091/why-i-am-getting-this-warning-message-does-not-conform-to-the-required-format
    document.getElementById("todays-date").addEventListener("load", dateToday);
    function dateToday() {
        const todayDate = new Date(); 
        const formatDate = todayDate.getDate() < 10 ? `0${todayDate.getDate()}`:todayDate.getDate();
        const formatMonth = todayDate.getMonth() < 10 ? `0${todayDate.getMonth()+1}`: todayDate.getMonth()+1;
        const formattedDate = [todayDate.getFullYear(), formatMonth, formatDate].join('-');
        document.getElementById('todays-date').value = formattedDate;
    }
    dateToday()
    // DATE MAX: Ensures Users cannot choose a date that is later than the current date.
    // Taken from: https://stackoverflow.com/questions/32378590/set-date-input-fields-max-date-to-today
    document.getElementById('todays-date').max = new Date().toISOString().split("T")[0];


    // Call hccTotal function on page load
    // hccTotal();
    
    
})

// Makes a modal display on a page when User lands on it. Used for when a User initially
// lands on a page and we require some data. Once the data has been provided, it must
// not display again. Function needs to be updated for the latter.
// Taken from https://www.tutorialrepublic.com/faq/how-to-launch-bootstrap-modal-on-page-load.php
$(document).ready(function(){
    $("#page-setup-modal").modal('show');
});


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



// Sales Methods & Units Function to ensure at least one checkbox
// is checked in each section before next page can be loaded
// Taken from (kind of): https://www.javascripttutorial.net/javascript-dom/javascript-form/
function injectHref() {
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
function displaySelectLabel(id) {
    console.log("Float Label fn fires");
    document.getElementById(id).style.display = "block";
    if (id==='select-recipient-label') {
        checkAndToggleHCCDivVisibility();
    }
}

// function hideSelectLabel(id) {
//     document.getElementById(id).style.display = "none";
// }

function checkAndToggleHCCDivVisibility() {
    const dropdown = document.getElementById('recipients')
    if (dropdown.options[dropdown.selectedIndex].id === "individual-birds") {
        document.getElementById('hcc-container-div').style.display = "block";
    } else {
        document.getElementById('hcc-container-div').style.display = "none";
    }
}

// Medicines Auto-Suggest: Set of functions that auto-suggests medicines in the db once the User begins typing
function setInputTextMedicine(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('medicine-suggestions-list').style.display = "none";
}
function showSuggestionsMedicines(value, labelId) {
    if (value.length) {
        // displaySelectLabel(labelId)
        let suggestions = '';
        MEDICINES.filter(item => item.medicine_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            suggestions += `<div onclick="setInputTextMedicine('medicine-name', '${item.medicine_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.medicine_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('medicine-suggestions-list').innerHTML = suggestions;
            // console.log("Suggestions :", suggestions);
            document.getElementById('medicine-suggestions-list').style.display = "block";
        } else {
            document.getElementById('medicine-suggestions-list').style.display = "none";
        }
    } else {
        // hideSelectLabel(labelId)
        document.getElementById('medicine-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu39b.gitpod.io/health_and_welfare/get_medicines')
.then(response => response.json())
.then(data => {
    MEDICINES = data.medicines;
});

// Diseases Auto-Suggest: Set of functions that auto-suggests diseases in the db once the User begins typing
function setInputTextDisease(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('disease-suggestions-list').style.display = "none";
}
function showSuggestionsDiseases(value, labelId) {
    if (value.length) {
        // displaySelectLabel(labelId)
        let suggestions = '';
        DISEASES.filter(item => item.disease_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            suggestions += `<div onclick="setInputTextDisease('disease-protected-against', '${item.disease_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.disease_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('disease-suggestions-list').innerHTML = suggestions;
            document.getElementById('disease-suggestions-list').style.display = "block";
        } else {
            document.getElementById('disease-suggestions-list').style.display = "none";
        }
    } else {
        // hideSelectLabel(labelId)
        document.getElementById('disease-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu39b.gitpod.io/health_and_welfare/get_diseases')
.then(response => response.json())
.then(data => {
    DISEASES = data.diseases;
});


// Vaccines Auto-Suggest: Set of functions that auto-suggests vaccines in the db once the User begins typing
function setInputTextVaccine(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('vaccine-suggestions-list').style.display = "none";
}
function showSuggestionsVaccines(value, labelId) {
    if (value.length) {
        // displaySelectLabel(labelId)
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
        // hideSelectLabel(labelId)
        document.getElementById('vaccine-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu39b.gitpod.io/health_and_welfare/get_vaccines')
.then(response => response.json())
.then(data => {
    VACCINES = data.vaccines;
});

// Viruses Auto-Suggest: Set of functions that auto-suggests viruses in the db once the User begins typing
function setInputTextVirus(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('virus-suggestions-list').style.display = "none";
}
function showSuggestionsViruses(value, labelId) {
    if (value.length) {
        // displaySelectLabel(labelId)
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
        // hideSelectLabel(labelId)
        document.getElementById('virus-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu39b.gitpod.io/health_and_welfare/get_viruses')
.then(response => response.json())
.then(data => {
    VIRUSES = data.viruses;
});
