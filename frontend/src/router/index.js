import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/terms',
    name: 'terms',
    component: () => import(/* webpackChunkName: "politics" */ '../views/TermsView.vue')
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: () => import(/* webpackChunkName: "faq" */ '../views/FAQ.vue')
  },
  {
    path: '/data',
    name: 'data',
    component: () => import(/* webpackChunkName: "data" */ '../views/DataPrivacyView.vue')
  },
  {
    path: '/install',
    name: 'install',
    component: () => import(/* webpackChunkName: "install" */ '../views/InstallView.vue')
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  { path: '/:pathMatch(.*)*', component: () => import(/* webpackChunkName: "about" */ '../views/NotFound.vue') },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
