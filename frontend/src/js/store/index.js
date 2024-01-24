/**
 * Creates vue store for website state management.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/index.js
 * @exports Store Created Store
 */

// Base imports.
import { createStore } from 'vuex'

// Store extensions.
import { mutations } from '@app/js/store/mutations'
import actions from '@app/js/store/actions'
import plugins from '@app/js/store/plugins'
import initialState from '@app/js/store/state'

// Create the actual store.
export default createStore({
    state: initialState,
    getters: {
        server_data(state) {
            return state.server_data
        },
        global_variables(state) {
            return state.global_variables
        },
        csrf_token(state) {
            return state.csrf_token
        },
        isLoading(state) {
            return state.isLoading
        },
        apiRequest(state) {
            return state.apiRequest
        },
        city(state) {
            return state.city
        },
        toast(state) {
            return state.toast
        },
    },
    actions,
    mutations,
    plugins
})