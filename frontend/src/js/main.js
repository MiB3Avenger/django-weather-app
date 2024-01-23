/**
 * Imports for main.js.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/main.js
 * @exports None
 */

/**
 * Vue imports.
 */
import 'vite/modulepreload-polyfill'
import { createApp } from 'vue'

/**
 * Application imports.
 */
import router from './router'
import store from './store'
import { loadFonts } from './plugins/webfontloader'
import App from './App.vue'

/**
 * Style imports.
 */
import "@app/css/style.scss"

/**
 * Prepare dependencies before creating vue app.
 */
loadFonts()

/**
 * Create vue app.
 */
createApp(App)
    // Inject application dependencies.
    .use(router)
    .use(store)
    .mount('#app')
