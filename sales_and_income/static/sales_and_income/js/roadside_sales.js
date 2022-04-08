$(document).ready(function() {
    console.log("Roadside sales Document ready!");
    var single_egg_price = Number(document.querySelector('input[name=single_egg_price]').value);
    var half_dozen_eggs_price = Number(document.querySelector('input[name=half_dozen_eggs_price]').value);
    var ten_eggs_price = Number(document.querySelector('input[name=ten_eggs_price]').value);
    var dozen_eggs_price = Number(document.querySelector('input[name=dozen_eggs_price]').value);
    var trays_of_eggs_price = Number(document.querySelector('input[name=trays_of_eggs_price]').value);
    // var qty_single_eggs_in_stock = Number(document.querySelector('input[name=qty_single_eggs_in_stock]').value);
    // var qty_single_eggs_remaining = Number(document.querySelector('input[name=qty_single_eggs_remaining]').value);
    // var qty_single_eggs_added = Number(document.querySelector('input[name=qty_single_eggs_added]').value);
    // var qty_half_dozen_egg_boxes_in_stock = Number(document.querySelector('input[name=qty_half_dozen_egg_boxes_in_stock]').value);
    // var qty_half_dozen_egg_boxes_remaining = Number(document.querySelector('input[name=qty_half_dozen_egg_boxes_remaining]').value);
    // var qty_half_dozen_egg_boxes_added = Number(document.querySelector('input[name=qty_half_dozen_egg_boxes_added]').value);
    // var qty_ten_egg_boxes_in_stock = Number(document.querySelector('input[name=qty_ten_egg_boxes_in_stock]').value);
    // var qty_ten_egg_boxes_remaining = Number(document.querySelector('input[name=qty_ten_egg_boxes_remaining]').value);
    // var qty_ten_egg_boxes_added = Number(document.querySelector('input[name=qty_ten_egg_boxes_added]').value);
    // var qty_dozen_egg_boxes_in_stock = Number(document.querySelector('input[name=qty_dozen_egg_boxes_in_stock]').value);
    // var qty_dozen_egg_boxes_remaining = Number(document.querySelector('input[name=qty_dozen_egg_boxes_remaining]').value);
    // var qty_dozen_egg_boxes_added = Number(document.querySelector('input[name=qty_dozen_egg_boxes_added]').value);
    // var qty_trays_eggs_in_stock = Number(document.querySelector('input[name=qty_trays_eggs_in_stock]').value);
    // var qty_trays_eggs_remaining = Number(document.querySelector('input[name=qty_trays_eggs_remaining]').value);
    // var qty_trays_eggs_added = Number(document.querySelector('input[name=qty_trays_eggs_added]').value);
    var qty_single_eggs_sold = 0;

    console.log('single_egg_price = ' + single_egg_price);
    console.log('half_dozen_eggs_price = ' + half_dozen_eggs_price);
    console.log('ten_eggs_price = ' + ten_eggs_price);
    console.log('dozen_eggs_price = ' + dozen_eggs_price);
    console.log('trays_of_eggs_price = ' + trays_of_eggs_price);
    //console.log('qty_single_eggs_in_stock = ' + qty_single_eggs_in_stock);
    document.querySelectorAll('input').forEach(item => {
        item.addEventListener('keyup', event => {
            // send request to latest no of trays
            console.log("item = ", item.value);
            single_egg_price = Number(document.querySelector('input[name=single_egg_price]').value);
            console.log('single_egg_price = ' + single_egg_price)
            console.log('type = ' + typeof(single_egg_price))
            var total = (single_egg_price + half_dozen_eggs_price)
            console.log('total test = ' + total)
            // var totalHens = document.querySelector('input[name=hens_qty]').value;
            // var totalChicks = document.querySelector('input[name=chicks_qty]').value;
            // var totalCocks = document.querySelector('input[name=cocks_qty]').value;
            // var total = Number(totalHens) + Number(totalChicks) + Number(totalCocks);
            // document.getElementById("total-birds").value = Number(total);
        })
    });
})

