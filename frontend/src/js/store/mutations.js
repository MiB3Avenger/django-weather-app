/**
 * Mutations for our store.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/plugins.js
 * @exports Object mutations
 */

// Base imports

// Export storage key
export const STORAGE_KEY = 'my-project-vuejs'

// For testing
if (navigator.webdriver) {
    window.localStorage.clear()
}

/* The `mutations` object is a collection of functions that are responsible for modifying the state of
the store in a Vuex application. Each function represents a specific mutation that can be triggered
to update the state. */
export const mutations = {
    // Any server data we get from server.
    server_data(state, server_data) {
        state.server_data = server_data
    },
    // Any global variables we get from server. Mostly API endpoints.
    global_variables(state, global_variables) {
        state.global_variables = global_variables
    },

    // state.state
    changeState(state, newState) {
        state.state = newState
    },
    resetState(state) {
        state.state = {}
    },

    // state.isLoading
    loading(state) {
        state.isLoading = true
    },
    loaded(state) {
        state.isLoading = false
    },

    // state.apiRequest
    setApiRequest(state) {
        state.apiRequest = true
    },
    resetApiRequest(state) {
        state.apiRequest = false
    },

    // state.city
    changeCity(state, newState) {
        state.city = newState
    },
    resetCity(state) {
        state.city = {}
    },

    // state.toast
    setToastData(state, data) {
        state.toast = data
    },
    dismissToast(state) {
        if(state.toast != undefined)
            state.toast.display = false
    },
}