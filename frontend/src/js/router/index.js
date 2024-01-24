import { createRouter, createWebHistory} from 'vue-router'

import Index from "@app/js/views/Index.vue"
import Detail from "@app/js/views/Detail.vue"
import FourOhFour from "@app/js/views/FourOhFour.vue"

const routes = [
    {
        path: '/',
        name: 'index',
        component: Index,
        meta: {
            title: 'Search for a city!'
        }
    },
    {
        path: '/city-detail/:country/:name',
        name: 'city-details',
        component: Detail,
        meta: {
            title: 'City Details'
        }
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'four-oh-four',
        component: FourOhFour,
        meta: {
            title: 'Uh oh!'
        }
    },
]

const router = createRouter({
    // In case we want to create url history
    base: "/",
    history: createWebHistory(),
    routes,
})

export default router