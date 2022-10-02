import { createApp } from 'vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import App from './App'

import "@/css/style.css"
import "@/css/style.less"
import "@/css/style.scss"

loadFonts()

createApp(App)
  .use(router)
  .use(vuetify)
  .use(store)
  .mount('#app')
