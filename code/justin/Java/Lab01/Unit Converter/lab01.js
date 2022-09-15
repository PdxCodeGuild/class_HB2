let measurements = {
    'ft':0.3048,
    'mi':1609.34,
    'm':1,
    'km':1000
}

function convert(){
    event.preventDefault();
    let meters = document.getElementById('meters').value;
    let units = document.getElementById('unit').value;
    let algo = meters * measurements[units];
    const para = document.createElement('p');
    para.innerText = meters + ' ' + units + ' ' + 'equals' + ' ' + algo + ' ' + 'meters';
    document.body.appendChild(para);}