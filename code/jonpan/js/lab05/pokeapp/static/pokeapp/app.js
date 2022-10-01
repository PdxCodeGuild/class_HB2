const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            message: "It works!",
            pokemon: [],
            searchTerm: null,
            page: 1,
            maxPage: 0,
        }
    },
    methods: {
        pokeSearch: function() {
            fetch(`/pokemon/?searchTerm=${this.searchTerm}&page=${this.page}`)
            .then(response => response.json())
            .then(data => {
            this.pokemon = data.data
            })
        },
        previousPage: function(){
            if (this.searchTerm === null) {
                if (this.page === 1) {
                    pass
                } else {
                    this.page -= 1
                    fetch(`/pokemon/?page=${this.page}`)
                    .then(response => response.json())
                    .then(data => {
                    this.pokemon = data.data
                    })
                }
            } else {
                if (this.page === 1) {
                    pass
                } else {
                    this.page -= 1
                    fetch(`/pokemon/?page=${this.page}&searchTerm=${this.searchTerm}`)
                    .then(response => response.json())
                    .then(data => {
                    this.pokemon = data.data
                    })
                }
            }
        },
        nextPage: function(){
            if (this.searchTerm === null) {
                if (this.page === this.maxPage) {
                    pass
                } else {
                    this.page += 1
                    fetch(`/pokemon/?page=${this.page}`)
                    .then(response => response.json())
                    .then(data => {
                    this.pokemon = data.data
                    })
                }
            } else {
                if (this.page === this.maxPage) {
                    pass
                } else {
                    this.page += 1
                    fetch(`/pokemon/?page=${this.page}&searchTerm=${this.searchTerm}`)
                    .then(response => response.json())
                    .then(data => {
                    this.pokemon = data.data
                    })
                }
            }
        },
    },
    watch: {
    },
    created: function() {
        fetch(`/pokemon/?page=${this.page}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.data, "hello")
            this.pokemon = data.data
            this.maxPage = data.data[this.pokemon.length -1]
            console.log(this.maxPage)
        })
    },
    mounted: function() {
    }
}).mount("#app")