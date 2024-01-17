/** @type {import('tailwindcss').Config} */
export default {
    darkMode: 'class',
    prefix: 'tw-',
    content: [
        './weather_app/templates/base.html',
        './weather_app/templates/**/*.html',
        './frontend/src/**/*.{js,ts,jsx,tsx,vue}'
    ],
    theme: {
        extend: {
            screens: {
                'xs': '576px'
            }
        },
        colors: {
            'white': '#ffffff',
            'black': '#000000',
            'grey': {
                50: '#F0F1F2',
                100: '#D1D3D8',
                200: '#BBBEC5',
                300: '#9CA1AA',
                400: '#898E99',
                500: '#6B7280',
                600: '#616874',
                700: '#4C515B',
                800: '#3B3F46',
                900: '#2D3036'
            },
            'primary': {
                50: '#EDEDFF',
                100: '#C7C8FE',
                200: '#ACAEFE',
                300: '#8688FD',
                400: '#6F71FD',
                500: '#4B4EFC',
                600: '#4447E5',
                700: '#3537B3',
                800: '#292B8B',
                900: '#20216A'
            },
            'success': {
                50: '#E9F9EF',
                100: '#BAEDCD',
                200: '#99E4B5',
                300: '#6BD893',
                400: '#4ED17E',
                500: '#22C55E',
                600: '#1FB356',
                700: '#188C43',
                800: '#136C34',
                900: '#0E5327'
            },
            'warning': {
                50: '#FEF5E7',
                100: '#FCE1B3',
                200: '#FAD28F',
                300: '#F8BE5C',
                400: '#F7B13C',
                500: '#F59E0B',
                600: '#DF900A',
                700: '#AE7008',
                800: '#875706',
                900: '#674205',
            },
            'error': {
                50: '#FDECEC',
                100: '#FAC5C5',
                200: '#F8A9A9',
                300: '#F48282',
                400: '#F26969',
                500: '#EF4444',
                600: '#D93E3E',
                700: '#AA3030',
                800: '#832525',
                900: '#641D1D'
            }
        }
    },
    plugins: [
        'postcss-import',
    ],
}
