import { defineConfig } from 'vite'

// https://vite.dev/config/

export default defineConfig({
  server: {
      proxy: {
          '/api': 'http://127.0.0.1:8000', // Proxy API calls to Django backend
      },
  },
});