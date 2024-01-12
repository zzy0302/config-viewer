import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  base: "",
  build: {
    outDir: "./dist",
    emptyOutDir: true,
    rollupOptions: {
      external: ["./utils/localStorage.js"]
    }
  },
  plugins: [vue()],
})
