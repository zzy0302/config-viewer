import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  base: "",
  build: {
    outDir: "./dist",
    emptyOutDir: true,
    rollupOptions: {},
  },
  plugins: [vue()],
  server: {
    port: 5000,
    proxy: {
      "/api": {
        target: "http://localhost:5052",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
