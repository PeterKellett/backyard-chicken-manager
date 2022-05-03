console.log("regular_tasks_coop_cleaning.js");

fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/regular_tasks/get_disinfectants')
.then(response => response.json())
.then(data => {
    console.log("Fetch disinfectant type fn fires");
    DISINFECTANTS = data.disinfectants;
    console.log("disinfectants Types :", DISINFECTANTS);
});

// Disinfectants Auto-Suggest: Set of functions that auto-suggests disinfectants from the db once the User begins typing
function setInputTextDisinfectant(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('disinfectant-suggestions-list').style.display = "none";
}

function showSuggestionsDisinfectants(value, labelId) {
    console.log("showSuggestionsDisinfectants")
    console.log("value.length" + value.length)
    if (value.length) {
        // displaySelectLabel(labelId)
        let suggestions = '';
        DISINFECTANTS.filter(item => item.disinfectant_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            console.log("disinfectant Type :", item.disinfectant_name);
            suggestions += `<div onclick="setInputTextDisinfectant('disinfectant-name', '${item.disinfectant_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.disinfectant_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('disinfectant-suggestions-list').innerHTML = suggestions;
            document.getElementById('disinfectant-suggestions-list').style.display = "block";
        } else {
            document.getElementById('disinfectant-suggestions-list').style.display = "none";
        }
    } else {
        // hideSelectLabel(labelId)
        document.getElementById('disinfectant-suggestions-list').style.display = "none";
    }
}

var form_data = {};
document.querySelectorAll('input').forEach(item => {
    form_data[item.name] = item.value;
    console.log("form_data = " + item.name + ": " + form_data[item.name])
})