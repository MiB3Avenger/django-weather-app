<script>
/**
* Main Vue Application
* 
* @author Chinmay Nagrale
* @version 0.1
* @file @js/App.vue
* @exports Object
*/

// Application imports.
import localForage from '@app/js/plugins/localforage'
import { STORAGE_KEY } from '@app/js/store/mutations'

export default {
    name: 'App',
    watch: {
        $route: {
            immediate: true,
            handler(to, from) {
                document.title = "Weather App | " + to.meta.title || "Weather App"
            }
        }
    },
    beforeMount() {
        let server_data = JSON.parse(document.getElementById('server_data').textContent);
        this.$store.commit("server_data", server_data)
    },
    beforeCreate() {
        localForage.getItem(STORAGE_KEY+"-city").then((value) => {
            // If the module data is not present, we will go to initial state of the modules.
            if(value == null)
                this.resetState()
            else
                this.$store.dispatch("changeCity", JSON.parse(value))
        })
    },
    computed: {
        server_data() {
            return this.$store.getters.server_data
        },
    },
    data() {
        return {
            
        }
    },
};
</script>

<template>
    <div>
        <router-view>
        </router-view>
    </div>
</template>