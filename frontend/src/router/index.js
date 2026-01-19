import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    // 这里不是自动加载的首页
    path: '/',
    name: 'home',
    component: () => import('../views/IndexView.vue'),
    children: [
      {
        path: '/home',
        name: '首页', // 中文名称
      },
      {
        path: '/home',
        name: 'Home',
        component: () => import('@/views/HomeView.vue'),
      },
      {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
          import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
      },
      {
        path: '/register',
        name: 'register',
        component: () => import('../views/RegisterView.vue'),
      },
      {
        path: '/login',
        name: 'login',
        component: () => import('../views/LoginView.vue'),
      },
      // Python 新书速递
      {
        path: '/book',
        name: 'BookList',
        component: () => import('../views/BookListView.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
