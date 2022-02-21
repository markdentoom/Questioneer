import { createRouter, createWebHistory } from "vue-router"
import Home from "../views/Home.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/ask/:slug?",
    name: "question-editor",
    component: () => import("../views/QuestionEditor.vue"),
    props: true,
  },
  {
    path: "/question/:slug",
    name: "question",
    // route level code-splitting
    // this generates a separate chunk (questioneer.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "questioneer" */ "../views/Question.vue"),
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory("/"),
  routes,
})

export default router
