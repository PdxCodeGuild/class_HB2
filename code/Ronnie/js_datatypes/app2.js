let fruits = ['apple', 'banana', 'orange']

// Create an unordered list
var list = document.createElement('ul');

// Create a list item for each wizard
// and append it to the list
fruits.forEach(function (fruit) {
	var li = document.createElement('li');
	li.innerText = fruit;
	list.appendChild(li);
});

let app = document.querySelector('#myApp');
app.appendChild(list);
