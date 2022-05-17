console.log("Regular tasks feeding time js start");

fetch('https:https://8000-peterkellet-backyardchi-59h2vqhodh4.ws-eu45.gitpod.io/regular_tasks/get_feeds')
.then(response => response.json())
.then(data => {
    console.log("Fetch feed type fn fires");
    FEEDS = data.feeds;
    console.log("Feed Types :", FEEDS);
});


// Function to automatically populate a unit of measurement
const measurementUnit = document.getElementById("weights-and-measures-units").value;
$("#unit-of-measurement").html(measurementUnit);


// Feeds Auto-Suggest: Set of functions that auto-suggests feeds from the db once the User begins typing
function setInputTextFeed(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('feed-suggestions-list').style.display = "none";
}

function showSuggestionsFeeds(value) {
    if (value.length) {
        let suggestions = '';
        FEEDS.filter(item => item.feed_name.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            console.log("Feed Type :", item.feed_name);
            suggestions += `<div onclick="setInputTextFeed('feed-name', '${item.feed_name}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.feed_name}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('feed-suggestions-list').innerHTML = suggestions;
            document.getElementById('feed-suggestions-list').style.display = "block";
        } else {
            document.getElementById('feed-suggestions-list').style.display = "none";
        }
    } else {
        document.getElementById('feed-suggestions-list').style.display = "none";
    }
}

function validate(event) {
    console.log("validate function");
    // document.getElementById('feed-suggestions-list').style.display = "none";
    // event.preventDefault();
}