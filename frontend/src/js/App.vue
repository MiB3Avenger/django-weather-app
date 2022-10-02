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
            <h4 class="text-h4">Conunter state: <em>{{counter}}</em></h4>

            <p class="">
              Data from the store that was passed from django via <code>json_script</code> template tag
            </p>
            <p>
              {{test}}
            </p>
          </div>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="8">
          <v-tabs>
            <v-tab link @click="$router.push('/')">
              Home ->
            </v-tab>
            <v-tab link @click="$router.push('/about')">
              About ->
            </v-tab>
          </v-tabs>
          <div>
            <v-fade-transition>
              <router-view />
            </v-fade-transition>
          </div>
        </v-col>
      </v-row>
    </v-main>
  </v-app>

</template>

<script>
export default {
  name: 'App',
  beforeMount() {
    let test = JSON.parse(document.getElementById('test').textContent);
    this.$store.commit("test", test)
  },
  computed: {
    test() {
      return this.$store.getters.test
    },
  },
  data() {
    return {
      counter: 0,
    }
  },
};
</script>