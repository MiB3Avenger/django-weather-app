import { createRouter, createWebHistory} from 'vue-router'

import About from "@app/js/components/About.vue"
import HelloWorld from "@app/js/components/HelloWorld.vue"

const routes = [
    { path: '/', component: HelloWorld },
    { path: '/about', component: About },
]

const router = createRouter({
    // In case we want to create url history
    base: "/",
    history: createWebHistory(),
    routes,
})

export default router