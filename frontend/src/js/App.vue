<script>
export default {
    name: 'App',
    beforeMount() {
        let server_data = JSON.parse(document.getElementById('server_data').textContent);
        this.$store.commit("server_data", server_data)
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