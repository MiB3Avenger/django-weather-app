/**
 * Helps keeping state in one single place without increasing scroll length in the createStore file.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/state.js
 * @exports Object Store Default State
 */

// Base imports. We create tailwind config, in case we want to specify how our graph should be coloured.
import resolveConfig from 'tailwindcss/resolveConfig'
import tailwindConfig from 'tailwind-config'

// Use tailwind config to access certain colors or other object properties to be instantiated before-hand.
const fullConfig = resolveConfig(tailwindConfig)

export default {
    // Any server data we get from server.
    server_data: {},
    // Any global variables we get from server. Mostly API endpoints.
    global_variables: {},
    // Project state.
    state: {},
    // CSRF Token for API request to Django backend.
    csrf_token: document.querySelector('[name=csrfmiddlewaretoken]').value,
    // Loading for whole application. We can keep track when the whole Vue App has been loaded.
    isLoading: true,
    // API Request State. We can see if there's a request made or not. Helps for waiting.
    apiRequest: false,
    // Toast Modal state structure.
    toast: {
        display: false,
        cleanToast: true,
        type: 'success',
        message: ''
    }
}