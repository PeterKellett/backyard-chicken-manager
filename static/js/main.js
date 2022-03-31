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

    // Show Hide Part 1: If a label is for a field that displays when a checkbox is checked this
    // function allows the label to display. Otherwise it shows up onscreen even though the input
    // it is for, doesn't.
    // DON'T THINK THIS IS REQUIRED. COMMENTED OUT TO SEE IF ANY ISSUES ARISE IN THE COMING WEEKS.
    // var checkbox = document.getElementById("disinfected");
    // checkbox.addEventListener('change', function() {
    //     if (this.checked) {
    //         document.getElementById("disinfectant-label").style.display="block";
    //         console.log("Checkbox is checked..");
    //     } else {
    //         document.getElementById("disinfectant-label").style.display="none";
    //         console.log("Checkbox is not checked..");
    //     }
    // });

    // Call hccTotal function on page load
    hccTotal();
    
// !!!!!!! (document).ready function end
})

// Show Hide Part 2: Function to display additional field(s) or content when a checkbox is checked
// Taken from http://jsfiddle.net/TrueBlueAussie/DLQY9/1/
$(function () {
    $('div.show-on-click').hide();
    console.log("Show on click fires");

    //show it when the checkbox is clicked
    $('input[class="click-to-show"]').on('click', function () {
        if ($(this).prop('checked')) {
            $('div.show-on-click').fadeIn();
        } else {
            $('div.show-on-click').hide();
        }
    });
});


// Show/Hide - Add Names: Function to display a text input when a User selects "Add Other" from a dropdown
function addName() {
    var dropdown = document.getElementById("medicine-name").value;
    if (dropdown === "Add Other") {
        document.getElementById("add-name-div").style.display="block";
        console.log("Add Other is chosen..");
    } else {
        document.getElementById("add-name-div").style.display="none";
        console.log("Add Other is not chosen..");
    }
};


// https://www.geeksforgeeks.org/how-to-pass-data-to-javascript-in-django-framework/
// fetch('https://8000-peterkellett-backyardchi-z5c38sm5p00.ws-eu38.gitpod.io/regular_tasks/js_test')
// .then(response => response.json())
// .then(data => {
//     console.log("DATA: ", data);
//     var dataNode = document.getElementById('alldata');
//     dataNode.innerHTML+="{{data|escapejs}}";
//     dataNode = document.getElementById('neatdata');
//     for(var x in data){
//             dataNode.innerHTML+=x+' : '+data[x]+'<br><br>';
//     }
// });


// Sales Methods & Units Function to ensure at least one checkbox
// is checked in each section before next page can be loaded
// Taken from (kind of): https://www.javascripttutorial.net/javascript-dom/javascript-form/
function injectHref() {
    console.log("Inject Href");
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


// Floating Input Labels: Display floating label on Select inputs when a selection is made
function displaySelectLabel() {
    console.log("displaySelectLabel Fires");
    document.getElementById('select-input-label').style.display = "block";
}
// Floating Input Labels: Display floating label on Select inputs when a selection is made
function displaySelectLabel2() {
    console.log("displaySelectLabel2 Fires");
    document.querySelectorAll('.select-input-label').style.display = "block";
}
