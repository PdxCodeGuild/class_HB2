const options = {
    headers: {'X-API-Key': 'pcDFqM1JDUUtsNyhkf4oE40QUpyC1So2ae4kMMaP'}
}
let congress_list = []

axios.get('https://api.propublica.org/congress/v1/116/senate/members.json', options).then((response) => {
    console.log(response.data)
    let congress = response.data['results'][0]['members'][0]
    for(item in congress){
        let first_name = item['first_name']
        congress_list.push(first_name)
    }
})
// Create an unordered list
var list = document.createElement('ul');
congress_list.forEach(function (member) {

    var li = document.createElement('li');
    li.innerText = member['first_name'];
    list.appendChild(li);
});
let app = document.querySelector('myApp')
app.appendChild(list)

