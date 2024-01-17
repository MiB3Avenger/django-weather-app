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

}