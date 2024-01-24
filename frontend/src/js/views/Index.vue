<script>
/**
 * Views: Index.
 * 
 * Index view for application.
 */


// Composable imports.
import useFrontend from '@app/js/composables/api/frontend'

export default {
    name: 'HelloWorld',
    data() {
        return {
            searchTerm: '',
            searchResults: [],
            frontend: useFrontend()
        }
    },
    methods: {
        handleInput: function() {
            // Debounce the search function to avoid making too many requests
            if (this.debouncedSearch) {
                clearTimeout(this.debouncedSearch)
            }
            this.debouncedSearch = setTimeout(() => {
                this.performSearch()
            }, 300); // Adjust the debounce delay as needed
        },
        performSearch: function() {
            // Fetch all the sponsors.
            this.frontend.getCityData(this.searchTerm).then((response) => {
                if(response.data.success) {
                    this.searchResults = response.data.locations
                }
            })
        },
        clearTerm: function() {
            this.searchTerm = ''
            this.searchResults = []
        },
        slugify: function(term) {
            return term.toLowerCase().replace(/[^a-zA-Z0-9]+/g, " ").trim().replace(" ", "-")
        },
        selectCity: function(city) {
            this.frontend.storeCityData(city).then((response) => {
                if(response.data.success) {
                    this.$router.push({ name: 'city-details', params: { country: city.country, name: this.slugify(city.name) } })
                }
            })
        }
    },
};
</script>

<template>
    <div>
        <h1>Search for a city to check forecast</h1>
        <div class="search-holder">
            <input v-model="searchTerm" @input="handleInput" placeholder="Search for a city name">
            <button @click="clearTerm">clear</button>
        </div>
        <ul>
            <li v-for="result in searchResults" :key="result.id">
                <a href="javascript:;" @click="selectCity(result)">{{ result.name }}, {{ result.country }}</a>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.search-holder {
    display: flex;
    height: 50px;

    clip-path: inset(0 0 0 0 round 25px);
    width: max-content;

    margin-bottom: 3rem;
    input {
        width: 400px;
        padding: 1rem;
        border-radius: 25px 0 0 25px;
        letter-spacing:1px;
        font-weight: 600;

        border: 1px solid #9CA1AA;
        border-right: 0;

        background: #fff;
        box-shadow: 0px 0px 0px 4px #D1D3D8;
    }
    button {
        width: 90px;
        border-radius: 0 25px 25px 0;
        color: #fff;
        line-height:45px;
        background-size: 300% 100%;
        letter-spacing:2px;
        font-weight: 600;
        border: 1px solid #9CA1AA;
        border-left: 0;
        
        transition: all .4s ease-in-out;
        
        background-image: linear-gradient(to right, #29323c, #485563, #2b5876, #4e4376);
        &:hover {
            cursor: pointer;
            color: #c1c1c1;
        }
    }
}

li {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 1rem;
}
</style>