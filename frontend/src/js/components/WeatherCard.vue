
<script>
/**
 * Component: WeatherCard.
 * 
 * Weather card component for application.
 */
export default {
    name: 'WeatherCard',
    props: {
        detail: Object,
    },
    data() {
        return {
            kel: 273.1
        }
    },
    methods: {
        degToDirection: (deg) => {
            if (deg >= 30 || deg < 330) return 'North'
            else if (deg > 30 && deg <= 60) return 'North East'
            else if (deg > 60 && deg <= 120) return 'East'
            else if (deg > 120 && deg <= 150) return 'South East'
            else if (deg > 150 && deg <= 210) return 'South'
            else if (deg > 210 && deg <= 240) return 'South West'
            else if (deg > 240 && deg <= 300) return 'West'
            else if (deg > 300 && deg <= 330) return 'North West'
            else return 'Invalid direction'
        }
    }
};
</script>

<template>
    <div class="weather-card">
        <div class="weather-details">
            <div class="time">
                {{ new Date(detail.reference_time * 1000).toUTCString() }}
            </div>
            <div class="cloud-temperature">
                <div class="icon" :class="{ 'sunny': detail.clouds < 20 && detail.humidity < 75, 'sunny-cloudy': detail.clouds >= 20 && detail.humidity < 75, 'sunny-cloudy-rainy': detail.clouds >= 20 && detail.humidity >= 65, 'cloudy-rain': detail.clouds >= 40 && detail.humidity >= 85, 'cloudy': detail.clouds >= 40 && detail.humidity >= 75 }"></div>
                <div class="degree-holder">
                    <div class="degree">
                        <span class="degree-value">{{ (detail.temperature.temp - kel).toFixed(2) }}</span>
                        <span class="cloud-status" style="text-transform: capitalize;">{{ detail.detailed_status }}</span>
                    </div>
                    <div class="degree-sign">°C</div>
                </div>
            </div>
            <div class="details-holder">
                <div class="details">
                    <div class="left"><div class="icon humidity"></div>Humidity</div>
                    <div class="right">{{ detail.humidity }}%</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon wind"></div>Wind Speed</div>
                    <div class="right">{{ detail.wind.speed }}m/s towards {{ degToDirection(detail.wind.deg) }}</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon wind"></div>Wind Gust</div>
                    <div class="right">Upto {{ detail.wind.gust }}m/s</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon temperature"></div>Temperature Feels Like</div>
                    <div class="right">{{ (detail.temperature.feels_like - kel).toFixed(2) }}°C</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon high-temperature"></div>Highest Temperature</div>
                    <div class="right">{{ (detail.temperature.temp_max - kel).toFixed(2) }}°C</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon low-temperature"></div>Lowest Temperature</div>
                    <div class="right">{{ (detail.temperature.temp_min - kel).toFixed(2) }}°C</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon pressure"></div>Pressure</div>
                    <div class="right">{{ detail.pressure.press }} hPa</div>
                </div>
                <div class="details">
                    <div class="left"><div class="icon pressure-sealevel"></div>Pressure at Sea Level</div>
                    <div class="right">{{ detail.pressure.sea_level }} hPa</div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.weather-card {
    display: flex;
    width: 400px;
    flex-direction: row;
    margin-bottom: 2rem;
    border: 1px solid;
    border-radius: .75rem;
    padding: 1.5rem;

    background: rgba(255, 255, 255, 0.29);

    box-shadow: 30px 30px 40px -10px rgba(0, 0, 0, 0.15);
    backdrop-filter: blur(5px);
    div.weather-details {
        display: flex;
        flex-direction: column;
        width: 100%;
        span.title {
            margin-right: 0.25rem;
            font-weight: 700;
            &::after {
                margin-left: .05rem;
                content: ':';
            }
        }
        .time {
            color: #7d7771;
        }
        .cloud-temperature {
            display: flex;
            padding: .5rem 0;
            justify-content: center;
            align-items: center;
            align-self: stretch;
            .icon {
                width: 100px;
                height: 100px;
                filter: drop-shadow(0px 9px 30px rgba(0, 0, 0, 0.05));
                *&::before {
                    display: block;
                    width: inherit;
                    height: 100%;
                    content: '';

                    background-repeat: no-repeat;
                    background-size: contain;
                }
                &.sunny {
                    &::before {
                        background-image: url('@app/assets/icons/weather/sunny.svg');
                    }
                }
                &.sunny-cloudy {
                    &::before {
                        background-image: url('@app/assets/icons/weather/sunny-cloudy.svg');
                    }
                }
                &.sunny-cloudy-rainy {
                    &::before {
                        background-image: url('@app/assets/icons/weather/sunny-cloudy-rainy.svg');
                    }
                }
                &.cloudy {
                    &::before {
                        background-image: url('@app/assets/icons/weather/cloudy.svg');
                    }
                }
                &.cloudy-rain {
                    &::before {
                        background-image: url('@app/assets/icons/weather/cloudy-rain.svg');
                    }
                }
            }
            .degree-holder {
                display: flex;
                justify-content: center;
                align-items: flex-start;
                .degree {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    gap: -5px;
                    text-align: center;
                    .degree-value {
                        font-size: 43px;
                        font-style: normal;
                        font-weight: 700;
                        line-height: normal;
                    }
                    .cloud-status {
                        font-size: 19px;
                        font-style: normal;
                        font-weight: 400;
                        line-height: normal;
                    }
                }
                .degree-sign {
                    display: flex;
                    align-items: center;
                    gap: 2px;
                    font-size: 14px;
                    font-style: normal;
                    font-weight: 300;
                }
            }
        }
        .details-holder {
            display: flex;
            padding: 10px 8px;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            align-self: stretch;
            .details {
                display: flex;
                padding: 14px 11px;
                justify-content: center;
                align-items: center;
                align-self: stretch;

                border-radius: 10px;
                border: 0.5px solid rgba(255, 255, 255, 0.50);
                background: rgba(255, 255, 255, 0.36);

                color: #303345;
                font-weight: 600;
                font-size: 14px;
                .left {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    margin-right: 5px;
                    .icon {
                        border-radius: 8px;
                        background: rgba(255, 255, 255, 0.90);
                        box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.07), 0px 9px 10px -3px rgba(23, 126, 37, 0.15);

                        width: 28px;
                        height: 28px;

                        background-repeat: no-repeat;
                        background-size: contain;

                        &.humidity {
                            background-image: url('@app/assets/icons/weather/humidity.svg');
                        }
                        &.wind {
                            background-image: url('@app/assets/icons/weather/wind.svg');
                        }
                        &.temperature {
                            background-image: url('@app/assets/icons/weather/umbrella.svg');
                        }
                    }
                }
                .right {
                    display: flex;
                    padding-right: 10px;
                    justify-content: flex-end;
                    align-items: center;
                    flex: 1 0 0;
                    font-weight: 400;
                }
            }

        }
    }
}
</style>