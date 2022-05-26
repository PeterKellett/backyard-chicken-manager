$(document).ready(function(){
    console.log("Regular tasks feeding time js start");
    $("#food-remaining-div").hide();
    $("#food-added-div").hide();
    $("#feeder-amount-div").hide();
    // $('body').click(function() {
    //     document.getElementById('feed-suggestions-list').style.display = "none";
    //     feed = $('#feed-name').val();
    //     console.log("feed = ", feed);
    //     setInputFields(feed);
    // })
});
fetch('https://8000-peterkellet-backyardchi-6r0pf5jpjxn.ws-eu45.gitpod.io/regular_tasks/get_feeds')
.then(response => response.json())
.then(data => {
    console.log("Fetch feed type fn fires");
    FEEDS = data.feeds;
    console.log("Feed Types :", FEEDS);
});

// Add an event listener to the flock field
document.getElementsByName("flock").forEach(item => {
    item.addEventListener("change", getPreviousFeedingTimes)
 })

var previous_feedings = [];
function getPreviousFeedingTimes() {
    console.log("getPreviousFeedingTimes")
    fetch(`https://8000-peterkellet-backyardchi-6r0pf5jpjxn.ws-eu45.gitpod.io/regular_tasks/get_flock_feeds/${this.value}`)
    .then(response => response.json())
    .then(data => {
        previous_feedings = data;  
    });  
}


// This function is run when a user has typed a feed name into the feed_name input.
// It compares the text in the feed_name input to the list of feed_name in the previous_feeds list.
// If the feed_name matches with a previous feed_name it shows the relevant fields to the user 
// and sets the 'required' attribute accordingly.
function setInputFields (feed) {
    console.log("setInputFields")
    console.log("feedinput = ", feed)
    console.log("previous_feedings = ", previous_feedings)
    if (previous_feedings.length > 0) {
        for (i = 0; i < previous_feedings.length; i++) {
            console.log("i = ", previous_feedings[i])
            if (previous_feedings[i].feed_name.toLowerCase() == feed.toLowerCase()) {
                $('#food-remaining-div').show().find('input').prop('required', true);
                $("#food-added-div").show().find('input').prop('required', true);
                $("#feeder-amount-div").hide().find('input').prop('required', false);
                break;
            }
            else {
                $("#feeder-amount-div").show().find('input').prop('required', true);
                $("#food-remaining-div").hide().find('input').prop('required', false);
                $("#food-added-div").hide().find('input').prop('required', false);
            }
        }
    }
    else {
        $("#feeder-amount-div").show().find('input').prop('required', true);
        $("#food-remaining-div").hide().find('input').prop('required', false);
        $("#food-added-div").hide().find('input').prop('required', false);
    }
}


// Function to automatically populate a unit of measurement
const measurementUnit = document.getElementById("weights-and-measures-units").value;
$("#unit-of-measurement").html(measurementUnit);


// Feeds Auto-Suggest: Set of functions that auto-suggests feeds from the db once the User begins typing
function setInputTextFeed(inputId, text) {
    console.log("inputId = ", inputId)
    console.log("text = ", text)
    document.getElementById(inputId).value = text;
    document.getElementById('feed-suggestions-list').style.display = "none";
    setInputFields(text);
}

function showSuggestionsFeeds(value) {
    console.log("showSuggestionsFeeds(value) = ", value)
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
            setInputFields(value) // Pass in the string from the feed_name input
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