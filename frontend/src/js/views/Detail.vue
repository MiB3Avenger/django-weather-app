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

export default {
    name: 'Detail',
    setup() {
        const store = useStore()
        const frontend = useFrontend()

        const kel = 273.1

        let city = computed(() => store.getters.city)

        const detail = reactive({})

        frontend.getCityDetails(city.value.name, city.value.country).then(response => {
            if(response.data.success)
            detail.value = {city: response.data.city, weather: response.data.weather}
        })

        return { kel, detail, city }
    }
};
</script>

<template>
    <div>
        <h1>Forecast for <span>{{ city.name }}</span></h1>
        <div>
            <ul>
                <li v-for="result in detail.value.weather">
                    {{ new Date(result.reference_time * 1000).toUTCString() }},
                    {{ result.clouds }},
                    {{ result.status }},
                    <span style="text-transform: capitalize;">{{ result.detailed_status }}</span>,
                    {{ result.humidity }},
                    {{ result.wind.speed }},
                    {{ result.wind.deg }},
                    {{ result.wind.gust }},
                    {{ (result.temperature.temp - kel).toFixed(2) }},
                    {{ (result.temperature.temp_max - kel).toFixed(2) }},
                    {{ (result.temperature.temp_min - kel).toFixed(2) }},
                    {{ (result.temperature.feels_like - kel).toFixed(2) }},
                    {{ result.pressure.press }} Ba,
                    {{ result.pressure.sea_level }} Ba
                </li>
            </ul>

        </div>
    </div>
</template>