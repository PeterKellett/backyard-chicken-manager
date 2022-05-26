$(document).ready(function(){
    console.log("Regular tasks watering time js start");
    $("#water-remaining-div").hide();
    $("#water-added-div").hide();
    $("#water-total-div").hide();
});

// Add an event listener to the flock field
document.getElementsByName("flock").forEach(item => {
    item.addEventListener("change", getPreviousWateringTimes)
 })

var previous_waterings = [];
function getPreviousWateringTimes() {
    console.log("getPreviousWateringTimes")
    fetch(`https://8000-peterkellet-backyardchi-6r0pf5jpjxn.ws-eu45.gitpod.io/regular_tasks/get_flock_waterings/${this.value}`)
    .then(response => response.json())
    .then(data => {
        previous_waterings = data;
        console.log(".then")
        console.log("previous_waterings :", previous_waterings);
    if (previous_waterings.length > 0) {
        $("#water-remaining-div").show().find('input').prop('required', true);;
        $("#water-added-div").show().find('input').prop('required', true);;
        $("#water-total-div").hide().find('input').prop('required', false);;
    }
    else {
        $("#water-remaining-div").hide().find('input').prop('required', false);;
        $("#water-added-div").hide().find('input').prop('required', false);;
        $("#water-total-div").show().find('input').prop('required', true);;
    }

    });
    
}

function validate(event) {
    console.log("validate function");
    // document.getElementById('feed-suggestions-list').style.display = "none";
    // event.preventDefault();
}