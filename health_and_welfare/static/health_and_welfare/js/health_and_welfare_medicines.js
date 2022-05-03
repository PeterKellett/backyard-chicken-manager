console.log("health_and_welfare_medicines.js");

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
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/health_and_welfare/get_medicines')
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
fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/health_and_welfare/get_diseases')
.then(response => response.json())
.then(data => {
    DISEASES = data.diseases;
});
