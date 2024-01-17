/**
 * Plugin actions for our store.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/store/plugins.js
 * @exports function Store Plugin
 */

// Base plugin imports.
import { createLogger } from 'vuex'
import { STORAGE_KEY } from './mutations'
import localForage from '@app/js/plugins/localforage'

/**
 * Creates a localstorage plugin and helps subscribe data into user's browser.
 * 
 * @param {Store} store 
 */
const localStoragePlugin = store => {
    // Subscribe to state.
    store.subscribe((mutation, { state }) => {
        localForage.setItem(STORAGE_KEY+"-state", JSON.stringify(state))
    })
}

// Decide whether to create a logger or not based on environment.
export default process.env.NODE_ENV !== 'production'
    ? [createLogger(), localStoragePlugin]
    : [localStoragePlugin]