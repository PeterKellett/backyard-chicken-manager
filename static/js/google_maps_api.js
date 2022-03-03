// Functions (2) to autosuggest cities.
// Taken from https://www.youtube.com/watch?v=c3MjU9E9buQ&t=165s
let autocomplete;
function initAutocomplete() {
    console.log("Map Called");
    autocomplete = new google.maps.places.Autocomplete(
        document.getElementById('city-country'),
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
        document.getElementById('city-country').placeholder =
        'Enter a City or Town';
    } else {
        document.getElementById('city-country').innerHTML = place.name;
    }
}