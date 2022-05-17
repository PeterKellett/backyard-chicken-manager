console.log("health_and_welfare_vaccines.js");

// Vaccines Auto-Suggest: Set of functions that auto-suggests vaccines in the db once the User begins typing
function setInputTextVaccine(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('vaccine-suggestions-list').style.display = "none";
}
function showSuggestionsVaccines(value, labelId) {
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
        // hideSelectLabel(labelId)
        document.getElementById('vaccine-suggestions-list').style.display = "none";
    }
}
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/health_and_welfare/get_vaccines')
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
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/health_and_welfare/get_viruses')
.then(response => response.json())
.then(data => {
    VIRUSES = data.viruses;
});
