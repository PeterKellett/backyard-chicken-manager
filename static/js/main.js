$(document).ready(function () {
    console.log("Document ready!");

    // PK function
    var flock_form_iteration = 0;
    function addFlockForm() {
        console.log("flock_form_iteration " + flock_form_iteration);
        $("#form-data").append(
            `<!-- Flock Core Info Section -->
            <section name="flock-core-info">
                <div>
                    <input type="text" name="flock_name" placeholder="Flock Name" id="flock_name" required>
                </div>
                <div>
                    {% if 'acquired_date' in onboard_profile_data %}
                    <input type="date" name="acquired_date" value="{{ onboard_profile_data.acquired_date }}" placeholder="Acquired Date" id="acquired_date" required>
                    {% else %}
                    <input type="date" name="acquired_date" placeholder="Acquired Date" id="acquired_date" required>
                    {% endif %}
                </div>
                <div>
                    <input type="text" name="coop1_name" placeholder="Coop Name" id="coop1_name" required>
                </div>
                <div>
                    <select name="breed" id="breed" required>
                        {% if 'breed' in onboard_profile_data %}
                        <option value="" disabled>Breed</option>
                            {% for breed in breed %}
                                {% if breed == onboard_Profile_data.breed %}
                                <option value="{{ breed }}" selected>{{ breed|title }}</option>
                                {% else %}
                                <option value="{{ breed }}">{{ breed|title }}</option>
                                {% endif %}
                            {% endfor %}
                        {% else %}     
                        <option value="" disabled selected>Breed</option>
                            {% for breed in breed %}
                            <option value="{{ breed }}">{{ breed|title }}</option>
                            {% endfor %}
                        {% endif %}
                    </select>
                </div>
                <!-- <div class="form-data">
                    <div>
                        <select name="purpose" id="purpose" required>
                            {% if 'purpose' in onboard_profile_data %}
                            <option value="" disabled>Purpose</option>
                            {% for purpose in purpose %}
                                {% if purpose == onboard_Profile_data.purpose %}
                                <option value="{{ purpose }}" selected>{{ purpose|title }}</option>
                                {% else %}
                                <option value="{{ purpose }}">{{ purpose|title }}</option>
                                {% endif %}
                            {% endfor %}
                        {% else %}     
                        <option value="" disabled selected>Purpose</option>
                            {% for purpose in purpose %}
                            <option value="{{ purpose }}">{{ purpose|title }}</option>
                            {% endfor %}
                        {% endif %}
                        </select>
                    </div>
                </div> -->
                <div>
                    <hr class="hr-small">
                </div>
            </section>`
        )
        flock_form_iteration++; // Increments the iteration by +1 
    }
    //addFlockForm();
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

    // HCC: Calculation to sum total number of birds
    document.getElementById("cocks-qty").addEventListener("onchange", hccTotal);
    function hccTotal() {
        console.log("hccTotal function")
        var totalHens = document.querySelector('input[name=hens_qty]').value;
        console.log("totalHens: " + totalHens);
        var totalChicks = document.querySelector('input[name=chicks_qty]').value;
        var totalCocks = document.querySelector('input[name=cocks_qty]').value;
        var total = Number(totalHens) + Number(totalChicks) + Number(totalCocks);
        console.log("totalBirds: " + total);
        document.getElementById("total-birds").textContent = total;
    }
    
    // HCC Section: Ensures at least one quantity is indicated
    function validateQtys() {
        if (document.getElementById('total-birds').value == null) {
            document.getElementById("bird-qty-warning").textContent =
                "Please provide at least one quantity for Hens, Chicks or Cocks.";
            return false;
            console.log("validateQtys: false");
        } else {
            console.log("validateQtys: true");
        }
    }
    
// !!!!!!! (document).ready function end
})


// Sales Methods & Units Function to ensure at least one checkbox
// is checked in each section before next page can be loaded
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
        document.getElementById("produce-next-button").href = "{% url 'onboard_stock' %}";
        document.getElementById("submit-form").submit();
        console.log("if true" )
    } else {
        document.getElementById('sales-unit-method-warning').textContent =
            "Please select at least one option each from Sales Methods and Sales Units";
            document.getElementById("submit-form").addEventListener('submit', (event) => {
                // stop form submission
                event.preventDefault();
            });
            console.log("if else" )
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
                            <input type="text" name="feed_name" placeholder="Feed Name" id="feed_name" required>
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
                                    <input type="text" name="supplement_name" placeholder="Supplement Name" id="supplement_name" required>
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
    $('input[name="disinfectant_name"]').hide();

    //show it when the checkbox is clicked
    $('input[name="disinfected-check"]').on('click', function () {
        if ($(this).prop('checked')) {
            $('input[name="disinfectant_name"]').fadeIn();
        } else {
            $('input[name="disinfectant_name"]').hide();
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

// Functions (2) to autosuggest cities.
// Taken from https://www.youtube.com/watch?v=c3MjU9E9buQ&t=165s
let autocomplete;
function initAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('city_country'),
        {
            // Don't know why it's not working when I include this. See table 3 in https://developers.google.com/maps/documentation/places/web-service/supported_types
            //types: ['cities'],
            fields: ['address_components','geometry'] //https://developers.google.com/maps/documentation/javascript/place-data-fields?hl=en
        });
    autocomplete.addListener('place_changed', onPlaceChanged);
    }

function onPlaceChanged() {
    var place = autocomplete.getPlace();

    if (!place.geometry) {
        document.getElementById('city_country').placeholder =
        'Enter a City or Town';
    } else {
        document.getElementById('city_country').innerHTML = place.name;
    }
}