// Egg Collection - Laid Calculation: Calculation to sum total number of eggs laid
var totalEggsLaid;
function totalEggsLaid() {
    var totalTrays = document.querySelector('input[name=qty_trays]').value;
    // trayQty needs to be updated to dynamically take in number of eggs per tray
    var trayQty = 30;
    var totalTraysQty = totalTrays * trayQty;
    var totalSingles = document.querySelector('input[name=qty_singles]').value;
    totalEggsLaid = Number(totalTraysQty) + Number(totalSingles);
    document.getElementById("total-eggs-laid").value = Number(totalEggsLaid);
}

// Egg Collection - Weight Calculation: Calculation to average weight of eggs laid
function averageEggWeight() {
    var totalWeight = document.querySelector('input[name=total_weight]').value;
    var brokenEggs = document.querySelector('input[name=eggs_broken]').value;
    var weighableEggs = totalEggsLaid - brokenEggs;
    var averageEggWeight = Number(totalWeight) / Number(weighableEggs);
    var averageEggWeightMetric = Math.ceil(averageEggWeight * 1000);
    document.getElementById("average-egg-weight").value = Number(averageEggWeightMetric);
    console.log("Average Egg Weight: " + averageEggWeightMetric);
}