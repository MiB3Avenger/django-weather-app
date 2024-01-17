/**
 * Composable: Progress.
 * 
 * This feature extends behaviour of progress bar. We can trigger entry and exit of progress bar using this composable.
 * It uses store to manage toast's state. Mostly accessed through axios instance or router instance.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/composables/progress.js
 * @exports function `useProgress`
 */

// Base import.
import store from "@app/js/store/index"

/**
 * Composable for progress bar feature. Export functions and variables for vue app to use.
 * 
 * @exports function `useProgress`
 * @returns The function `useProgress` returns an object with two methods: `getProgress`, `setProgress` and `resetProgress`.
 */
export default function useProgress() {
    const inProgress = store.getters.apiRequest

    /**
     * Sets progress bar to active. Uses action to trigger event.
     */
    const setProgress = () => {
        store.dispatch('setApiRequest')
    }

    /**
     * Sets progress bar to inactive. Uses action to trigger event.
     */
    const resetProgress = () => {
        store.dispatch('resetApiRequest')
    }


    /**
     * Fetches progress bar current state. Uses store getter to access state.
     * 
     * @returns {boolean} 
     */
    const getProgress = () => inProgress

    return { getProgress, setProgress, resetProgress }
}