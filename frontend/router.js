import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Questions from '~/pages/questions.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/questions', component: Questions, name: 'questions'}
  ],
  scrollBehavior () {
    return { x: 0, y: 0 }
  },
  prefetchLinks: false
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
