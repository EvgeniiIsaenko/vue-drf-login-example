import { createRouter, createWebHashHistory } from 'vue-router'
import RegView from '@/views/RegView'
import ProfileView from '@/views/ProfileView'

const routes = [
  {
    path: '/register',
    name: 'register',
    component: RegView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes,
})

export default router
