const { resolve } = require('path');
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import vuetify from 'vite-plugin-vuetify'


export default defineConfig({
  plugins: [
		vue(),
		vuetify({ autoImport: true }),
	],
  root: resolve('./frontend/src'),
  base: '/static/vite/',
  server: {
    host: true,
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.json', '.vue', '.less', '.scss'],
    alias: {
      '@': resolve(__dirname, './frontend/src'),
      '@js': resolve(__dirname, './frontend/src/js'),
      '@css': resolve(__dirname, './frontend/src/css'),
    },
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
    },
  },
});