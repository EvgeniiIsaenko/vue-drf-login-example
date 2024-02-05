import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import { createApp } from 'vue';

createApp(App).use(VueCookies).use(router).mount("#app");