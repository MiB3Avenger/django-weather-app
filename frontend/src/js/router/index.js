 import { createRouter, createWebHashHistory, createWebHistory} from 'vue-router'

import About from "@js/components/About.vue"
import HelloWorld from "@js/components/HelloWorld.vue"

const routes = [
  { path: '/', component: HelloWorld },
  { path: '/about', component: About },
]

const router = createRouter({
  // In case we want to create url history
  // history: createWebHistory(),
  // base: "/",
  history: createWebHashHistory(),
  routes,
})

export default router