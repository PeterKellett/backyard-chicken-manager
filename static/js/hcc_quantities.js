// HCC Section - Calculation: Calculation to sum total number of birds
function hccTotal() {
    var totalHens = document.querySelector('input[name=hens_qty]').value;
    var totalChicks = document.querySelector('input[name=chicks_qty]').value;
    var totalCocks = document.querySelector('input[name=cocks_qty]').value;
    var total = Number(totalHens) + Number(totalChicks) + Number(totalCocks);
    document.getElementById("total-birds").value = Number(total);
}

hccTotal();


// HCC Section - Validation: Ensures at least one quantity is indicated before user can move on
function validateFlock() {
    const flockName = document.getElementById('flock-name').value;
    const acquiredDate = document.getElementById('acquired-date').value;
    const coopName = document.getElementById('coop-name').value;
    const breed = document.getElementById('breed').value;
    const totalBirds = document.getElementById('total-birds').value;
    const totalBirdsNumber = Number(totalBirds);

    if (flockName == 0 ) {
        document.getElementById("warning-section-text").textContent =
            "Please provide a Flock Name";
        document.getElementById("submit-form").addEventListener('submit', (event) => {
            // stop form submission
            event.preventDefault();
        });
    } else {
        if (acquiredDate == 0 ) {
        document.getElementById("warning-section-text").textContent =
            "Please provide an Acquired Date";
        document.getElementById("submit-form").addEventListener('submit', (event) => {
            // stop form submission
            event.preventDefault();
        });
    } else {
        if (coopName == 0 ) {
        document.getElementById("warning-section-text").textContent =
            "Please provide a Coop Name";
        document.getElementById("submit-form").addEventListener('submit', (event) => {
            // stop form submission
            event.preventDefault();
        });
    } else {
        if (breed == 0 ) {
        document.getElementById("warning-section-text").textContent =
            "Please provide a Breed for your birds";
        document.getElementById("submit-form").addEventListener('submit', (event) => {
            // stop form submission
            event.preventDefault();
        });
    } else {
        if (totalBirdsNumber == 0 ) {
        document.getElementById("warning-section-text").textContent =
            "Please provide at least one quantity for Hens, Chicks or Cocks.";
        document.getElementById("submit-form").addEventListener('submit', (event) => {
            // stop form submission
            event.preventDefault();
        });
    } else {
    document.getElementById("submit-form").submit();
    }
}}}}
}

// This is a shorter less user pleasing version of the above. Left here in case the
// above doesn't work as well as hoped :-)
// HCC Section - Validation: Ensures at least one quantity is indicated before user can move on
//function validateFlock() {
//    const flockName = document.getElementById('flock-name').value;
//    const acquiredDate = document.getElementById('acquired-date').value;
//    const coopName = document.getElementById('coop-name').value;
//    const breed = document.getElementById('breed').value;
//    const totalBirds = document.getElementById('total-birds').value;
//    const totalBirdsNumber = Number(totalBirds);
//
//    if (totalBirdsNumber == 0 || flockName == 0 || acquiredDate == 0 || coopName == 0 || breed == 0) {
//        document.getElementById("warning-section-text").textContent =
//            "Please provide a Flock Name, Acquired Date, Coop Name, Breed and at least one quantity for Hens, Chicks or Cocks.";
//        document.getElementById("submit-form").addEventListener('submit', (event) => {
//            // stop form submission
//            event.preventDefault();
//        });
//    } else {
//        document.getElementById("submit-form").submit();
//    }
//}


function showHideHCC(value, idName) {
    if(value.length == 0) {
        $(`div.${idName}`).hide;
    } else {
        $(`div.${idName}`).fadeIn();
    }
}

