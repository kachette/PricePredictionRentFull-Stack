function onPageLoad() {
    console.log('document loaded');
    var url = 'http://127.0.0.1:5000/get_location_names';
    $.get(url, function(data, status) {
        console.log('got response for get_location_names request');
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById('uiLocations');
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

function getBedroomsValue() {
    var uiBedrooms = document.getElementById('uiBedrooms');
    for (var i in uiBedrooms) {
        if (uiBedrooms[i].checked) {
            return parseInt(i) + 1
        }
    }
    return -1;
}

function getBathValue() {
    var uiBathrooms = document.getElementById('uiBathrooms');
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log('price estimation clicked');
    var sqft = document.getElementById('uiSqft');
    var bedrooms = getBedroomsValue();
    var bath = getBathValue();
    var location = document.getElementById('uiLocations');
    var estPrice = document.getElementById('uiEstimatedPrice')
    var balcony = 1

    var url = 'http://127.0.0.1:5000/predict_home_price'

    $.post(url, {
        location: location.value,
        total_sqft: parseFloat(sqft.value),
        bath: bath,
        bedrooms: bedrooms,
        balcony: balcony
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = '<h2>' + data.estimated_price.toString() + '£';
        console.log(status);
    });

}

window.onload = onPageLoad