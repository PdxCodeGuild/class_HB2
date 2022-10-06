

axios({
  method: 'get',
  url: `/pokemon/`
})
  .then((response) => {
    console.log(response.data)
    document.getElementById("list").innerHTML = response.data

  })



function pokeSearch() {
        axios({
            method: 'get',
            url: `/pokemon/?searchTerm=${searchTerm}&page=${page}`
          })
            .then((response) => {
              console.log(response.data)
              document.getElementById("search-results").innerHTML = response.name

            })
        }
        












// pokeSearch: function() {
    
// },
// previousPage: function(){
//     if (this.searchTerm === null) {
//         if (this.page === 1) {
//             pass
//         } else {
//             this.page -= 1
//             fetch(`/pokemon/?page=${this.page}`)
//             .then(response => response.json())
//             .then(data => {
//             this.pokemon = data.data
//             })
//         }
//     } else {
//         if (this.page === 1) {
//             pass
//         } else {
//             this.page -= 1
//             fetch(`/pokemon/?page=${this.page}&searchTerm=${this.searchTerm}`)
//             .then(response => response.json())
//             .then(data => {
//             this.pokemon = data.data
//             })
//         }
//     }
// },
// nextPage: function(){
//     if (this.searchTerm === null) {
//         if (this.page === this.maxPage) {
//             pass
//         } else {
//             this.page += 1
//             fetch(`/pokemon/?page=${this.page}`)
//             .then(response => response.json())
//             .then(data => {
//             this.pokemon = data.data
//             })
//         }
//     } else {
//         if (this.page === this.maxPage) {
//             pass
//         } else {
//             this.page += 1
//             fetch(`/pokemon/?page=${this.page}&searchTerm=${this.searchTerm}`)
//             .then(response => response.json())
//             .then(data => {
//             this.pokemon = data.data
//             })
//         }
//     }
// },