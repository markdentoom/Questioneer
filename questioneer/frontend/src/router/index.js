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
    // route level code-splitting
    // this generates a separate chunk (questioneer.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "questioneer" */ "../views/QuestionEditor.vue"
      ),
    props: true,
  },
  {
    path: "/question/:slug",
    name: "question",
    component: () => import("../views/Question.vue"),
    props: true,
  },
  {
    path: "/answer/:uuid",
    name: "answer-editor",
    component: () => import("../views/AnswerEditor.vue"),
    props: true,
  },
  {
    path: "/:catchAll(.*)",
    name: "page-not-found",
    component: () => import("../views/NotFound.vue"),
  },
]

const router = createRouter({
  history: createWebHistory("/"),
  routes,
})

export default router
