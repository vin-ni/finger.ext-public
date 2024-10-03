// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  compatibilityDate: "2024-07-04",
  modules: ["@nuxtjs/tailwindcss", "shadcn-nuxt", '@pinia/nuxt'],
  ssr: false,
  runtimeConfig: {
    public: {
      esp32Ip: process.env.NUXT_PUBLIC_ESP32_IP
    }
  },
  devServer: {
    host: '127.0.0.1',
    port: 3000
  },
  shadcn: {
    /**
     * Prefix for all the imported component
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * @default "./components/ui"
     */
    componentDir: './components/ui'
  },
  css: ['~/assets/css/main.css', '~/assets/scss/main.scss'],
})