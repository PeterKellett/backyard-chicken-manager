console.log("health_and_welfare_supplements.js");

fetch('https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu43.gitpod.io/health_and_welfare/get_supplements')
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
        // displaySelectLabel(labelId)
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

document.querySelectorAll('input').forEach(item =>{
    console.log("item.name = " + item.name);
    console.log("item.value = " + item.value)
})