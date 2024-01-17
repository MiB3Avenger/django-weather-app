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
            counter: 0,
        }
    },
};
</script>

<template>
    <v-app>
        <v-main class="pa-3">
            <v-row justify="center">
                <v-col cols="10">
                    <div>
                        <h1 class="text-h1">Hello from Vuetify app</h1>
                        <p class="text-subtitle-1 mb-2">
                            Counter demo here!!!
                            <br>
                            <v-btn class="mr-2" @click.stop="counter++">Increase counter</v-btn>
                            <v-btn class="mr-2" @click.stop="counter--">Decrease counter</v-btn>
                            <v-btn class="mr-2" @click.stop="counter = 0">Reset counter</v-btn>
                        </p>
                        <p class="mb-4">
                            <v-btn class="mr-2" @click.stop="counter += 5">Increase counter by 5</v-btn>
                            <v-btn class="mr-2" @click.stop="counter -= 5">Decrease counter by 5</v-btn>
                        </p>
                        <h4 class="text-h4">Counter state: <em>{{counter}}</em></h4>

                        <p class="">
                            Data from the store that was passed from django via <code>json_script</code> template tag
                        </p>
                        <p>
                            {{ server_data }}
                        </p>
                    </div>
                </v-col>
            </v-row>
            <v-row justify="center">
                <v-col cols="8">
                    <v-tabs>
                        <v-tab to="/">
                            Home ->
                        </v-tab>
                        <v-tab to="/about">
                            About ->
                        </v-tab>
                    </v-tabs>
                    <div>
                        <router-view v-slot="{ Component, route }">
                            <v-fade-transition>
                                <component :is="Component" :key="route.path" />
                            </v-fade-transition>
                        </router-view>
                    </div>
                </v-col>
            </v-row>
        </v-main>
    </v-app>
</template>