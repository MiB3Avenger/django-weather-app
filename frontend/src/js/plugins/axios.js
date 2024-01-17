/**
 * An extended axios instance with progress bar hooked.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/plugins/axios.js
 * @exports AxiosInstance Instance
 */

// Base import.
import axios from "axios"

// Progress Bar import.
import useProgress from "@app/js/composables/progress"

// Fetch global variables from document.
// We cannot wait until store is ready and populated, so to make instance quickly, we use this method.
let global_variables = JSON.parse(document.getElementById('__globalVariables__') != null ? document.getElementById('__globalVariables__').textContent : "{}")
const api =  global_variables.urls.api ?? '/' // If there's no url for API, just use base url.

// Progress Bar start...
const { setProgress, resetProgress } = useProgress()

// Create instance...
const instance = axios.create({
    baseURL: api,
    headers: {"X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value}
});

// Extend functionality to handle progress bar...
instance.interceptors.request.use((config) => {
    setProgress() // for every request start the progress
    return config
});
instance.interceptors.response.use((response) => {
    resetProgress() // finish when a response is received
    return response
});

// Export the instance...
export default instance