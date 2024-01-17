const { resolve } = require('path');
import { fileURLToPath, URL } from "url"
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import vuetify from 'vite-plugin-vuetify'


export default defineConfig({
    plugins: [
        vue(),
        vuetify({ autoImport: true }),
    ],
    define: {
        // enable hydration mismatch details in production build
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false'
    },
    root: resolve('./frontend/src'),
    base: process.env.APP_ENV == 'prod' ? 'https://example.com' : 'http://localhost:3000/',
    server: {
        host: 'localhost',
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
        origin: process.env.APP_ENV == 'prod' ? 'https://example.com' : 'http://localhost:3000'
    },
    resolve: {
        extensions: ['.js', '.json', '.vue', '.less', '.scss'],
        alias: [
            { find: '@app', replacement: fileURLToPath(new URL('./frontend/src', import.meta.url)) },
            { find: 'tailwind-config', replacement: fileURLToPath(new URL('./tailwind.config.js', import.meta.url)) },
        ],
    },
    optimizeDeps: {
        include: ['tailwind-config'],
    },
    build: {
        outDir: resolve('./frontend/dist/vite'),
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                main: resolve('./frontend/src/js/main.js'),
                test: resolve('./frontend/src/js/test.js'),
            },
            output: {
                chunkFileNames: undefined,
            },
            external: [
                /^\/static\/.*/
            ]
        },
        commonjsOptions: {
            include: ['tailwind.config.js', 'node_modules/**']
        }
    },
});