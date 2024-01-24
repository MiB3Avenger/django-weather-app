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
        <input v-model="searchTerm" @input="handleInput" placeholder="Type to search">
        <button @click="clearTerm">clear</button>
        <ul>
            <li v-for="result in searchResults" :key="result.id">
                <a href="#" @click="selectCity(result)">{{ result.name }}</a>
            </li>
        </ul>
    </div>
</template>