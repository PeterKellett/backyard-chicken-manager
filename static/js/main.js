$(document).ready(function(){
    console.log("Document ready!")
  });


// Show Password. Taken from https://www.w3schools.com/howto/howto_js_toggle_password.asp
function showPasswordFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

// Calculation to sum total number of birds in HCC section
function hccTotal(){
    var totalHens = document.querySelector('input[name=hens-qty]').value;
    var totalChicks = document.querySelector('input[name=chicks-qty]').value;
    var totalCocks = document.querySelector('input[name=cocks-qty]').value;
    var total = Number(totalHens) + Number(totalChicks) + Number(totalCocks);
    document.getElementById("total-birds").textContent = total;
}

// HCC Section: Ensures at least one quantity is indicated
function validateQtys(){
    if( document.getElementById('total-birds').value == null){
        document.getElementById("bird-qty-warning").textContent = 
        "Please provide at least one quantity for Hens, Chicks or Cocks.";
        return false;
    }
}

// Sales Methods & Units Function to ensure at least one checkbox is checked
// in each section before next page can be loaded
function injectHref(){
    var salesMethods = null;
    var salesUnits = null;
    if( document.getElementById('roadside-check').checked == true ||
        document.getElementById('markets-check').checked == true ||
        document.getElementById('deliveries-check').checked == true ||
        document.getElementById('collections-check').checked == true) {
        salesMethods = true;
        } else {
          salesMethods = false
        }

    if( document.getElementById('single-eggs-check').checked == true ||
        document.getElementById('half-dozen-carton-check').checked == true ||
        document.getElementById('dozen-carton-check').checked == true ||
        document.getElementById('trays-check').checked == true ){
        salesUnits = true;
        } else {
          salesUnits = false
        }

    if (salesMethods == true && salesUnits == true){
        window.location.href = "{% url 'onboard_stock' %}";
        } else {
          document.getElementById('sales-unit-method-warning').textContent = 
          "Please select at least one option each from Sales Methods and Sales Units";
        }
    }

// Adds another set of fields fields when the "Add Another" button is clicked
function addAnotherFlock() {
    var flockCodeBlock = '<div>' +
                            '<hr class="hr-small">' +
                        '</div>' +
                            '<div class="container form-data">' +
                    '<div class="row mb-0" id="hens-row">' +
                        '<div class="col-1 col-css">' +
                            '<img src="{{ MEDIA_URL }}hen.png" alt="Chicken" class="col-css-element">' +
                        '</div>' +
                        '<div class="col-4 col-css">' +
                            '<h4 class="row-name col-css-element">Hens</h4>' +
                        '</div>' +
                        '<div class="col-3 col-css">' +
                            '<p class="checkbox-label hcc-checkbox-label col-css-element">All Hens</p>' +
                        '</div>' +
                        '<div class="col-1 col-css">' +
                            '<input type="checkbox" name="all_hens_check" id="all_hens_check" class="col-css-element hcc-checkbox">' +
                        '</div>' +
                        '<div class="col-3 col-css col-css-right">' +
                            '{% if "hens_qty" in onboard_profile_data %}' +
                            '<input type="number" name="hens-qty" value="{{ onboard_profile_data.hens_qty }}" placeholder="Qty" id="hens-qty" ' +
                                'step="1" min="0" oninput="this.value = Math.abs(this.value)" class="hcc-input" onkeyup="hccTotal()">' +
                            '{% else %}' +
                            '<input type="number" name="hens-qty" placeholder="Qty" id="hens_qty" ' +
                                'step="1" min="0" oninput="this.value = Math.abs(this.value)" class="hcc-input" onkeyup="hccTotal()">' +
                            '{% endif %}' +
                        '</div>' +
                    '</div>' +
                    '<div>' +
                        '<hr class="hr-small">' +
                    '</div>' +

                    '<div class="row mb-0" id="chicks-row">' +
                        '<div class="col-1 col-css">' +
                            '<img src="{{ MEDIA_URL }}hen.png" alt="Chicks" class="col-css-element">' +
                        '</div>' +
                        '<div class="col-4 col-css">' +
                            '<h4 class="row-name col-css-element">Chicks</h4>' +
                        '</div>' +
                        '<div class="col-3 col-css">' +
                            '<p class="checkbox-label hcc-checkbox-label col-css-element">All Chicks</p>' +
                        '</div>' +
                        '<div class="col-1 col-css">' +
                            '<input type="checkbox" name="all_chicks_check" id="all_chicks_check" class="col-css-element hcc-checkbox">' +
                        '</div>' +

                        '<div class="col-3 col-css col-css-right">' +
                            '{% if "chicks_qty" in onboard_profile_data %}' +
                            '<input type="number" name="chicks-qty" value="{{ onboard_profile_data.chicks_qty }}" placeholder="Qty" id="chicks-qty" ' +
                            'step="1" min="0" oninput="this.value = Math.abs(this.value)" class="hcc-input" onkeyup="hccTotal()">' +
                            '{% else %}' +
                            '<input type="number" name="chicks-qty" placeholder="Qty" id="chicks_qty" ' +
                                'step="1" min="0" oninput="this.value = Math.abs(this.value)" class="hcc-input" onkeyup="hccTotal()">' +
                            '{% endif %}' +

                        '</div>' +
                    '</div>' +
                    '<div>' +
                        '<hr class="hr-small">' +
                    '</div>' +

                    '<div class="row mb-0" id="cocks-row">' +
                        '<div class="col-1 col-css">' +
                            '<img src="{{ MEDIA_URL }}hen.png" alt="Cocks" class="col-css-element">' +
                        '</div>' +
                        '<div class="col-4 col-css">' +
                            '<h4 class="row-name col-css-element">Cocks</h4>' +
                        '</div>' +
                        '<div class="col-3 col-css">' +
                            '<p class="checkbox-label hcc-checkbox-label col-css-element">All Cocks</p>' +
                        '</div>' +
                        '<div class="col-1 col-css">' +
                            '<input type="checkbox" name="all_cocks_check" id="all_cocks_check" class="col-css-element hcc-checkbox">' +
                        '</div>' +
                        '<div class="col-3 col-css col-css-right">' +
                            '{% if "cocks_qty" in onboard_profile_data %}' +
                            '<input type="number" name="cocks-qty" value="{{ onboard_profile_data.cocks_qty }}" placeholder="Qty" id="cocks-qty" ' +
                            'step="1" min="0" oninput="this.value = Math.abs(this.value)" class="hcc-input" onkeyup="hccTotal()">' +
                            '{% else %}' +
                            '<input type="number" name="cocks-qty" placeholder="Qty" id="cocks-qty" ' +
                                'step="1" min="0" oninput="this.value = Math.abs(this.value)" class="hcc-input" onkeyup="hccTotal()">' +
                            '{% endif %}' +
                        '</div>' +
                    '</div>' +
                    '<div>' +
                        '<hr class="hr-small">' +
                    '</div>' +
                    '<div class="row mb-0">' +
                        '<div class="col-10 col-css">' +
                            '<h6 class="row-name">Total Number of Birds:</h6>' +
                        '</div>' +

                        '<div class="col-2 col-css col-css-right">' +
                            '<h6 id="total-birds">0</h6>' +
                        '</div>' +
                    '</div>' +
                '</div>';
    document.querySelector('div[name=flocks-container]').outerHTML = flockCodeBlock;
}

// Adds another set of feeds fields when the "Add Another" button is clicked
function addAnotherFeed() {
    var feedsCodeBlock = `<div class="row">
                            <hr class="hr-small">
                        </div>
                        <div class="row">
                            <input type="text" name="feed_name" placeholder="Feed Name" id="feed_name" required>
                        </div>
                        <div class="container">
                            <div class="row">
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
                        <div class="container" name="feeds-container"></div>`
    document.querySelector('div[name=feeds-container]').outerHTML = feedsCodeBlock;
}

// Adds another set of supplements fields when the "Add Another" button is clicked
function addAnotherSupplement() {
    var supplementsCodeBlock = '<div class="row">' +
                                    '<hr class="hr-small">' +
                                '</div>' +
                                '<div class="row">' +
                                    '<input type="text" name="supplement_name" placeholder="Supplement Name" id="supplement_name" required>' +
                                '</div>' +
                                '<div class="container">' +
                                    '<div class="row">' +
                                        '<div class="col-10 col-css">' +
                                            '<input type="number" name="supplement-amount-stock" placeholder="Amount in Stock" id="supplement-amount-stock" ' +
                                                'step="1" min="0" oninput="this.value = Math.abs(this.value)" required>' +
                                    '</div>' +
                                    '<div class="col-2 col-css">' +
                                        '<h5 class="text-end">' +
                                            'ml' +
                                        '</h5>' +
                                    '</div>' +
                                '</div>' +
                                '<div class="container" name="supplements-container"></div>';
    document.querySelector('div[name=supplements-container]').outerHTML = supplementsCodeBlock;
}

// Functions to autosuggest cities
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

// Function to make textarea height to expand based on amopunt of text added by the user
// Taken from https://www.techiedelight.com/automatically-resize-textarea-height-javascript/
$(document).ready(function() {
    $('textarea').on('keyup keypress', function() {
        $(this).height(0);
        $(this).height(this.scrollHeight);
    });
});