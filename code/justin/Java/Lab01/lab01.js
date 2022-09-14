let measurements = {
    'ft':0.3048,
    'mi':1609.34,
    'm':1,
    'km':1000
}

function convert(){
    let meters = document.getElementById('meters').value;
    let units = document.getElementById('unit').value;
    alert(meters + ' ' + units);
}