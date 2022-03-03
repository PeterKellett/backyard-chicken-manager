$(document).ready(function () {
    console.log("Document ready!");
  
    // PK function
    var flock_form_iteration = 0;
    function addFlockForm() {
        console.log("flock_form_iteration " + flock_form_iteration);
        $("#form-data").append(
            `<section name="flock-core-info">
            <div class="bottom-margin">
                {% if 'flock_name' in onboard_profile_data %}
                <input type="text" name="flock_name" value="{{ onboard_profile_data.flock_name }}" placeholder="Flock Name" id="flock-name" autofocus required>
                {% else %}
                <input type="text" name="flock_name" placeholder="Flock Name" id="flock-name" autofocus required>
                {% endif %}
            </div>
            <div class="bottom-margin">
                {% if 'acquired_date' in onboard_profile_data %}
                <input type="date" name="acquired_date" value="{{ onboard_profile_data.acquired_date }}" placeholder="Acquired Date" id="acquired-date" required>
                {% else %}
                <input type="date" name="acquired_date" placeholder="Acquired Date" id="acquired-date" required>
                {% endif %}
            </div>
            <div class="bottom-margin">
                {% if 'coop_name' in onboard_profile_data %}
                <input type="text" name="coop_name" value="{{ onboard_profile_data.coop_name }}" placeholder="Coop Name" id="coop-name" required>
                {% else %}
                <input type="text" name="coop_name" placeholder="Coop Name" id="coop-name" required>
                {% endif %}
            </div>
            <div class="bottom-margin">
                <select name="breed" id="breed" required>
                    {% if 'breed' in onboard_profile_data %}
                    <option value="" disabled>Breed</option>
                        {% for breed in breed %}
                            {% if breed.id == onboard_profile_data.breed %}
                            <option value="{{ breed.id }}" selected>{{ breed|title }}</option>
                            {% else %}
                            <option value="{{ breed.id }}">{{ breed|title }}</option>
                            {% endif %}
                        {% endfor %}
                    {% else %}     
                    <option value="" disabled selected>Breed</option>
                        {% for breed in breed %}
                        <option value="{{ breed.id }}">{{ breed|title }}</option>
                        {% endfor %}
                    {% endif %}
                </select>
                       
                <div class="bottom-margin">
                    <hr class="hr-small">
                </div>
            </div>
        </section>`
        )
        flock_form_iteration++; // Increments the iteration by +1 
    }
    // addFlockForm();
    $("#PKaddAnotherFlock").click(function () {
        addFlockForm();
    })

    // Show Password. Taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
    function showPasswordFunction() {
        var x = document.getElementById("password");
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
    }

    // Floating Input Labels: If a label is for a field that displays when a checkbox is checked this
    // function allows the label to display. Otherwise it shows up onscreen even though the input
    // it is for, doesn't.
    var checkbox = document.getElementById("disinfected");
    checkbox.addEventListener('change', function() {
        if (this.checked) {
            document.getElementById("disinfectant-label").style.display="block";
            console.log("Checkbox is checked..");
        } else {
            document.getElementById("disinfectant-label").style.display="none";
            console.log("Checkbox is not checked..");
        }
    });

    // Call hccTotal function on page load
    hccTotal();
    
// !!!!!!! (document).ready function end
})



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


// FLOCKS: Adds another set of fields fields when the "Add Another" button is clicked
function addAnotherFlock() {
    var flockCodeBlock = `{% include 'html_includes/hens_chicks_cocks.html' %}`;
    document.querySelector('div[name=flocks-container]').outerHTML = flockCodeBlock;
    }


// FEEDS: Adds another set of fields when the "Add Another" button is clicked
function addAnotherFeed() {
    var feedsCodeBlock = `<div class="bottom-margin">
                            <hr class="hr-small">
                        </div>
                        <div class="bottom-margin">
                            <input type="text" name="feed_name" placeholder="Feed Name" id="feed-name" required>
                        </div>
                        <div class="container">
                            <div class="row bottom-margin">
                                <div class="col-10 col-css">
                                    <input type="number" name="feed-qty-stock" placeholder="Qty in Stock" id="feed-qty-stock"
                                        step="1" min="0" oninput="this.value = Math.abs(this.value)" required>
                                </div>
                                <div class="col-2 col-css">
                                    <h5 class="text-end">
                                        kg
                                    </h5>
                                </div>
                            </div>
                        </div>
                        <div class="container" name="feeds-container">
                        </div>`
        document.querySelector('div[name=feeds-container]').outerHTML = feedsCodeBlock;
        }


// SUPPLEMENTS: Adds another set of fields when the "Add Another" button is clicked
function addAnotherSupplement() {
    var supplementsCodeBlock = `<div class="bottom-margin">
                                    <hr class="hr-small">
                                </div>
                                <div class="bottom-margin">
                                    <input type="text" name="supplement_name" placeholder="Supplement Name" id="supplement-name" required>
                                </div>
                                <div class="container">
                                    <div class="row bottom-margin">
                                        <div class="col-10 col-css">
                                            <input type="number" name="supplement-amount-stock" placeholder="Amount in Stock" id="supplement-amount-stock" 
                                                step="1" min="0" oninput="this.value = Math.abs(this.value)" required>
                                        </div>
                                        <div class="col-2 col-css">
                                            <h5 class="text-end">
                                                ml
                                            </h5>
                                        </div>
                                    </div>
                                </div>
                                <div class="container" name="supplements-container">
                                </div>`;
    document.querySelector('div[name=supplements-container]').outerHTML = supplementsCodeBlock;
    }


// Function to display additional fields or content when a checkbpx is checked
// Taken from http://jsfiddle.net/TrueBlueAussie/DLQY9/1/
$(function () {
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


