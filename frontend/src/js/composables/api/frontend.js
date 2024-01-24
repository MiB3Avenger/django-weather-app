/**
 * Composable: Frontend API.
 * 
 * This composable allows us to interact with Frontend API and contains support functions
 * to help make successful API calls.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/composables/api/modules.js
 * @exports function `useFrontend`
 */

// Base imports
import { ref } from "vue"

// Plugins and composable imports
import instance from "@app/js/plugins/axios"
import store from "@app/js/store/index"
import useProgress from "@app/js/composables/progress"


/**
 * The `useFrontend` function returns an object with methods for subscribing to a newsletter,
 * submitting a contact form, submitting a sponsor form, and retrieving sponsors.
 * 
 * @exports function `useFrontend`
 * @returns The function `useFrontend` returns an object with the following properties:
 * `subscribeToNewsletterForm`, `contactForm`, `sponsorForm`, `getSponsors`, and `getSponsorsTierOne`.
 */
export default function useFrontend() {
    // Initial parameters.
    // Store
    const isLoading = ref(false)
    const errors = ref({})

    // Composable objects
    const { resetProgress } = useProgress()

    const slugify = (term) => {
        return term.toLowerCase().replace(/[^a-zA-Z0-9]+/g, " ").trim().replace(" ", "-")
    }

    /**
     * The function `getCityData` makes a GET request to retrieve city names.
     * @param name - The name parameter is the city name user wants to search for.
     * @returns The function `getCityData` returns a promise.
     */
    const getCityData = (name) => {
        // Decline any request until existing request isn't fulfilled.
        if(isLoading.value) return

        isLoading.value = true

        // Return a promise with cities.
        return instance.get('frontend/search/city/'+slugify(name))
            .finally(() => {
                isLoading.value = false 
                resetProgress()
            })
    }

    /**
     * The function `storeCityData` makes a POST request to store selected city.
     * @param data - Object with city data which is to be stored/retrieved from database if it's data is present.
     * @returns The function `storeCityData` returns a promise.
     */
    const storeCityData = (data) => {
        // Decline any request until existing request isn't fulfilled.
        if(isLoading.value) return

        isLoading.value = true

        const body = {
            name: data.name,
            slug: slugify(data.name),
            country: data.country,
            lat: data.coordinates.lat,
            lon: data.coordinates.lon
        }

        // Return a promise with storing city.
        return instance.post('frontend/store/city', body)
            .finally(() => {
                // Dispatch response to store our data.
                store.dispatch("changeCity", body)
                isLoading.value = false 
                resetProgress()
            })
    }

    /**
     * The function `storeCityData` makes a POST request to store selected city.
     * @param name - The name of city.
     * @param country - City's residing country code.
     * @returns The function `storeCityData` returns a promise.
     */
    const getCityDetails = (name, country) => {
        // Decline any request until existing request isn't fulfilled.
        if(isLoading.value) return

        isLoading.value = true

        // Return a promise with cities.
        return instance.get('frontend/search/city-detail/'+country+'/'+slugify(name))
            .finally(() => {
                isLoading.value = false 
                resetProgress()
            })
    }

    return { getCityData, storeCityData, getCityDetails, slugify }
}