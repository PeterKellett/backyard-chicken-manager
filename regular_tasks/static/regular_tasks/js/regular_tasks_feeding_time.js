console.log("Regular tasks feeding time js start");

fetch('https://8000-peterkellett-backyardchi-trwsv0uk1lf.ws-eu34.gitpod.io/regular_tasks/get_feeds')
.then(response => response.json())
.then(data => {
    console.log("Fetch feed type fn fires");
    FEEDS = data.feeds;
    console.log("Feed Types :", FEEDS);
});

// Feeds Auto-Suggest: Set of functions that auto-suggests feeds from the db once the User begins typing
function setInputTextFeed(inputId, text) {
    document.getElementById(inputId).value = text;
    document.getElementById('feed-suggestions-list').style.display = "none";
}

function showSuggestionsFeeds(value, labelId) {
    if (value.length) {
        // displaySelectLabel(labelId)
        let suggestions = '';
        FEEDS.filter(item => item.feed_type.toLowerCase().includes(value.toLowerCase())).forEach(item => {
            console.log("Feed Type :", item.feed_type);
            suggestions += `<div onclick="setInputTextFeed('feed-type', '${item.feed_type}')" style="padding: 1px 15px; text-align: left; cursor: pointer; font-size: medium;">${item.feed_type}</div>`;
        });
        if (suggestions.length) {
            document.getElementById('feed-suggestions-list').innerHTML = suggestions;
            document.getElementById('feed-suggestions-list').style.display = "block";
        } else {
            document.getElementById('feed-suggestions-list').style.display = "none";
        }
    } else {
        // hideSelectLabel(labelId)
        document.getElementById('feed-suggestions-list').style.display = "none";
    }
}

function validate(event) {
    console.log("validate function");
    // event.preventDefault();
}