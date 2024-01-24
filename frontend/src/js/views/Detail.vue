<script>
/**
 * Views: Detail.
 * 
 * Detail view for application.
 */
// Base imports
import { ref, reactive, computed } from 'vue'
import { useStore } from 'vuex'

// Composable imports.
import useFrontend from '@app/js/composables/api/frontend'
import WeatherCard from '@app/js/components/WeatherCard.vue'

export default {
    name: 'Detail',
    components: {
        WeatherCard,
    },
    setup() {
        const store = useStore()
        const frontend = useFrontend()

        let city = computed(() => store.getters.city)

        const detail = reactive({})

        frontend.getCityDetails(city.value.name, city.value.country).then(response => {
            if(response.data.success)
            detail.value = {city: response.data.city, weather: response.data.weather}
        })

        return { detail, city }
    }
};
</script>

<template>
    <div>
        <h1>Forecast in <span>{{ city.name }}</span> for next 5 days at 3 hours interval</h1>
        <div class="weather-container">
            <WeatherCard v-for="result in detail.value?.weather" :detail="result"></WeatherCard>
        </div>
    </div>
</template>

<style scoped>
.weather-container {
    display: flex;
    width: -webkit-fill-available;
    width: fill-available;
    flex-direction: row;
    align-items: stretch;
    gap: 2rem;
    flex-shrink: 0;
    flex-wrap: wrap;
    justify-content: center;
}
span {
    font-style: italic;
}
</style>