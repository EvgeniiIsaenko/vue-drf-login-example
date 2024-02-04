import { createRouter, createWebHashHistory } from 'vue-router'
import RegView from '@/views/RegView'

const routes = [
  {
    path: '/reg',
    name: 'reg',
    component: RegView,
  },
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
})

export default router
